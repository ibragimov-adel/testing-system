from django.db import models
import tests.helpers as helpers
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone

class Test(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название теста")
    evaluated = models.BooleanField(verbose_name="Оцениваемый")
    code = models.CharField(max_length=5, default=helpers.random_code, verbose_name="Код")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null = True, verbose_name="Автор")

class Question(models.Model):
    test = models.ForeignKey(Test,on_delete=models.CASCADE, null = True, verbose_name = "Тест")
    text = models.TextField(verbose_name="Текст вопроса")
    answer = models.CharField(max_length=30, verbose_name="Ответ")
    points = models.IntegerField(default=0, verbose_name="Количество баллов за вопрос")


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null = True, verbose_name = "Вопрос")
    text = models.CharField(max_length = 30, verbose_name = "Текст")
    is_correct = models.BooleanField(verbose_name = "Корректность")


class Result(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null = True, verbose_name = "Тест")
    name = models.CharField(max_length = 20, verbose_name = "Имя")
    total_points = models.IntegerField(default = 0, verbose_name = "Баллы")
    date = models.DateTimeField(auto_now_add = True, blank = True, verbose_name = "Дата")
