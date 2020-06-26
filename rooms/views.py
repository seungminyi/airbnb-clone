from django.db.models import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView
from . import models

# Create your views here.
class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    ordering = ["pk"]


class RoomDetail(DetailView):
    model = models.Room

