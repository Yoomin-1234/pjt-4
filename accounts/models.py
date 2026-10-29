from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    GENDER_CHOICES = [
        ('남성', '남성'),
        ('여성', '여성'),
    ]

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, verbose_name='성별')
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name='나이')
    weekly_reading_time = models.PositiveIntegerField(null=True, blank=True, verbose_name='주간 평균 독서 시간(시간)')
    annual_reading_count = models.PositiveIntegerField(null=True, blank=True, verbose_name='연간 독서량(권)')
    interested_genres = models.CharField(max_length=600, blank=True, verbose_name='관심 장르')