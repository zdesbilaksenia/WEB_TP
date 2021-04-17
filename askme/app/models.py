from django.db import models

# Create your models here.

class Author(models.Model):
	name = models.CharField(max_length=255)
	birth_date = models.DateField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Автор'
		verbose_name_plural = 'Авторы'

class Article(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	author = models.ForeignKey('Author', on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'