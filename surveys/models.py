from django.db import models


class Survey(models.Model):
    # Главная таблица для опросов
    title = models.CharField(max_length=50)
    start_at = models.DateField()
    finish_at = models.DateField()
    description = models.CharField(max_length=512)


class QuestionTypes(models.Model):
    # Таблица типов вопросов (1 - один вариант, 2 - несколько вариантов, 3 - текстовый ответ)
    name = models.CharField(max_length=20)


class Question(models.Model):
    # Таблица вопросов
    question = models.CharField(max_length=512)
    type = models.ForeignKey(QuestionTypes, on_delete=models.CASCADE, related_name='question')
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='question')


class AnswerVariant(models.Model):
    # Таблица с вариантами ответов на вопросы
    title = models.CharField(max_length=120)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answervariant')


class UserAnswer(models.Model):
    # Таблица с ответами пользователей
    user = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='useranswer')
    answer = models.CharField(max_length=512)
