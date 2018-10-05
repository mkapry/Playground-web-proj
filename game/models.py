# -*-coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
import core.models


class Course(models.Model):
    """
    Поле
    заполняется админом
    """
    name = models.CharField(max_length=100)
    par = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    """
    Игра
    создает пользователь на фронте
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.IntegerField(default=0, blank=True, null=True)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, null=True)

    def __str__(self):
        return '{} {} {}'.format(self.course.name, self.user, self.score)


class Stats(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shot = models.CharField(max_length=100)

    def __str__(self):
        return '{} {}'.format(self.user, self.game.course)


class Hole(models.Model):
    """
    Лунка
    добавляет админ
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    par = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.course.name, self.number)


class HoleStats(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField()
    hole = models.ForeignKey(Hole, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.hole.course, self.hole.number)
