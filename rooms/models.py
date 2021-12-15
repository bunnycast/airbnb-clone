from django.db import models
from django_countries.fields import CountryField

from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):
    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """RoomType Model Definition"""

    pass

    class Meta:
        verbose_name = "Room Type"
        ordering = ["name"]


class Amenity(AbstractItem):

    """Amenity Model Definition"""

    pass

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """Facility Model Definition"""

    pass

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """HouseRule Model Definition"""

    pass

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):

    """Photo model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey(
        "rooms.Room", related_name="photos", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):

    """Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()

    # django-countries library 활용
    country = CountryField()

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

    # room => user ForeignKey N:1
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    room_type = models.ForeignKey(
        "rooms.RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )

    # Room <=> RoomItem 상속받은 모델 (Facility, Amenity, HouseRule) MTM 연결
    facilities = models.ManyToManyField(
        "rooms.Facility", related_name="rooms", blank=True
    )
    amenities = models.ManyToManyField(
        "rooms.Amenity", related_name="rooms", blank=True
    )
    house_rules = models.ManyToManyField(
        "rooms.HouseRule", related_name="rooms", blank=True
    )

    # 객체를 전달할 때 표시되는 이름을 변경
    def __str__(self):
        return self.name

    def total_rating(self):
        all_reviews = self.review.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating_average()
        return all_ratings / len(all_reviews)

    total_rating.short_description = "Total Rating⭐️"
