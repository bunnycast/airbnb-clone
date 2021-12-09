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

    """ RoomType Model Definition"""

    pass


class Amenity(AbstractItem):

    """ Amenity Model Definition """

    pass


class Facility(AbstractItem):

    """ Facility Model Definition """

    pass


class HouseRule(AbstractItem):

    """ HouseRule Model Definition """

    pass


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
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)

    # Room <=> RoomItem 상속받은 모델 (Facility, Amenity, HouseRule) MTM 연결
    facilities = models.ManyToManyField(Facility, blank=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    house_rules = models.ManyToManyField(HouseRule, blank=True)

    # 객체를 전달할 때 표시되는 이림을 변경
    def __str__(self):
        return self.name
