from django.db import models
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    title = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Amenity(AbstractItem):
    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    class Meta:
        verbose_name_plural = "Facilities"


class Rule(AbstractItem):
    class Meta:
        verbose_name_plural = "Rules"


class RoomType(AbstractItem):
    class Meta:
        verbose_name_plural = "Room Types"


class Room(core_models.TimeStampedModel):

    name = models.CharField(max_length=150)
    description = models.TextField()
    city = models.CharField(max_length=80)
    address = models.CharField(max_length=200)
    price_per_hour = models.IntegerField()
    capacity = models.IntegerField()
    amenities = models.ManyToManyField(Amenity, related_name="rooms", blank=True)
    facilities = models.ManyToManyField(Facility, related_name="rooms", blank=True)
    room_types = models.ForeignKey(
        RoomType, related_name="rooms", on_delete=models.CASCADE, default="Select",
    )
    is_wind_possible = models.BooleanField(default=False)
    is_percussion_possible = models.BooleanField(default=False)
    rules = models.ManyToManyField(Rule, related_name="rooms", blank=True)
    all_day = models.BooleanField(default=False)
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)


class Photo(core_models.TimeStampedModel):
    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
