from django.db import models
from datetime import date
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.all().order_by("-date")

    def hot(self):
        return self.all().order_by("-rating")

    def tag(self, tag):
        return self.all().filter(tags__name=tag)

    def one_question(self, pk):
        return self.filter(id=pk)


class Question(models.Model):
    author = models.ForeignKey("Profile", on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    text = models.TextField()
    date = models.DateField(default=date.today)
    tags = models.ManyToManyField("Tag")
    rating = models.IntegerField(default=0)

    objects = QuestionManager()

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    author = models.ForeignKey("Profile", on_delete=models.CASCADE)
    text = models.TextField()
    correct = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    def __str__(self):
        return self.question.title


class Tag(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default="img/avatar.png")
    login = models.CharField(max_length=32)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return self.login


class LikeToQuestion(models.Model):
    user = models.ForeignKey("Profile", on_delete=models.CASCADE)
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    like = 1
    dislike = -1
    no_like = 0
    like_choice = [(like, "like"), (dislike, "dislike"), (no_like, "no_like")]

    is_liked = models.SmallIntegerField(choices=like_choice, default=no_like)

    class Meta:
        verbose_name = "Лайк на вопросе"
        verbose_name_plural = "Лайки на вопросе"

    def __str__(self):
        return self.user.login + " оценил " + self.question.title


class LikeToAnswer(models.Model):
    user = models.ForeignKey("Profile", on_delete=models.CASCADE)
    answer = models.ForeignKey("Answer", on_delete=models.CASCADE)
    like = 1
    dislike = -1
    no_like = 0
    like_choice = [(like, "like"), (dislike, "dislike"), (no_like, "no_like")]

    is_liked = models.SmallIntegerField(choices=like_choice, default=no_like)

    class Meta:
        verbose_name = "Лайк на ответе"
        verbose_name_plural = "Лайки на ответе"

    def __str__(self):
        return self.user.login + " оценил " + self.answer.question.title
