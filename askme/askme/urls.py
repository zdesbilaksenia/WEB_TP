from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ask/', views.ask, name="ask"),
    path('login/', views.login, name="login"),
    path('settings/', views.settings, name="settings"),
    path('signup/', views.signup, name="signup"),
    path('tag/<str:tag_name>/', views.tag, name="tag"),
    path('question/<int:pk>/', views.question, name="question"),
    path('hot/', views.hotquestions, name="hot"),
    path('', views.index, name="index")
]
