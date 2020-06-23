from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.House_rules)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic info",
            {"fields": ("name", "description", "contry", "address", "price")},
        ),
        ("Time", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths",)}),
        (
            "More About Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules",),
            },
        ),
        ("Last Detailes", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "contry",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_ameneities",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "contry",
    )
    search_fields = ("=city", "host__username")

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    raw_id_fields = ("host",)

    def save_model(self, request, obj, form, change):
        print(obj, change, form)
        super().save_model(request, obj, form, change)

    def count_ameneities(self, obj):
        return "potato"

    count_ameneities.short_description = "hello"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = (
        "__str__",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width=100px src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
