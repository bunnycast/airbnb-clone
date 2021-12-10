from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    # admin > 목록 페이지에서 보여줄 필드를 설정
    list_display = (
        "name",
        "country",
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
        "count_amenities",
        # "facilities"
        # "house_rules",
    )

    # admin > 목록 페이지에서 필터링 할 필드를 지정
    list_filter = (
        "instant_book",
        "room_type",
        "facilities",
        "amenities",
        "house_rules",
        "city",
        "country",
    )

    # admin > 목록 페이지에서 검색할 필드 지정 (prefix : ^startswith =iexact @search None)
    search_fields = ("=city", "^host__username")

    # admin > 요소 페이지에서 수평 위젯으로 추가 가능
    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Time", {"fields": ("check_in", "check_out")}),
        (
            "More About the Space",
            {
                # 메뉴 접기 기능
                "classes": ("collapse",),
                "fields": (
                    "amenities",
                    "facilities",
                    "house_rules",
                ),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    # Using Admin Function
    def count_amenities(self, obj):
        print(obj.amenities)
        return None

    count_amenities.short_description = "super sexy"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    pass
