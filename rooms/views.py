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
    room_type = int(request.GET.get("room_type",0))
    room_types = models.RoomType.objects.all()
    price = int(request.GET.get("price",0))
    guests = int(request.GET.get("guests",0))
    beds = int(request.GET.get("beds",0))
    bedrooms = int(request.GET.get("bedrooms",0))
    baths = int(request.GET.get("baths",0))
    instant = request.GET.get("instant", False)
    super_host = request.GET.get("super_host",False)
    s_amenities = request.GET.getlist("amenities")
    s_facilities = request.GET.getlist("facilities")

    form = {"city": city,
            "s_room_type": room_type,
            "s_country": country,
            "price": price,
            "guests": guests,
            "beds": beds,
            "bedrooms": bedrooms,
            "baths": baths,
            "s_amenities": s_amenities,
            "s_facilities": s_facilities,
            "instant": instant,
            "super_host": super_host,
            }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    choices = {"countries": Countries, "room_types": room_types, "amenities" : amenities, "facilities" : facilities}

    return render(request, "rooms/search.html", {**form, **choices},)

