from django.db import models


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    # time Stamp 를 사용하는 모든 app 모델에 상속하는 추상 모델 (DB에 등록되지 않음) // migration 필요 없음
