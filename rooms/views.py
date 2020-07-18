from django.db.models import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView
from django_countries import Countries
from . import models

# Create your views here.
class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    ordering = ["pk"]


class RoomDetail(DetailView):
    model = models.Room


def search(request):

    city = request.GET.get("city", "")
    city = str.capitalize(city)
    country = request.GET.get("country")
    room_type = int(request.GET.get("room_type"))
    room_types = models.RoomType.objects.all()

    form = {"city": city, "s_room_type": room_type, "s_country": country}

    choices = {"countries": Countries, "room_types": room_types}

    return render(request, "rooms/search.html", {**form, **choices},)

