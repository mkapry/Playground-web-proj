from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
from django.views.generic import ListView, CreateView

from game.models import Course, Game


class CoursePage(ListView):
    template_name = "game/courses.html"
    model = Course


class GameCreateView(CreateView):
    model = Game
    fields = ('course', 'user')


def stats(request):
    return HttpResponse('Statistics')


def game(request):
    return HttpResponse('Game')


def total(request):
    return HttpResponse('Total')


def course(request):
    return HttpResponse('Course')
