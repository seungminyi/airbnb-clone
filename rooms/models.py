from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

# Create your models here.


class AbstactItem(core_models.TimeStampedModel):

    """ Abstact Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstactItem):
    pass

    class Meta:
        verbose_name = "Room Type"
        ordering = ["created"]


class Amenity(AbstactItem):
    pass

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstactItem):
    pass

    class Meta:
        verbose_name_plural = "Facilities"


class House_rules(AbstactItem):
    pass

    class Meta:
        verbose_name = "House Rule"


class Room(core_models.TimeStampedModel):
    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    contry = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    house_rules = models.ManyToManyField(House_rules, blank=True)

    def __str__(self):
        return self.name
