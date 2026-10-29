from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Book(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="도서 제목",
    )
    description = models.TextField(
        verbose_name="도서 설명",
    )
    customer_review_rank = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ],
        verbose_name="회원 리뷰 평점",
    )
    author = models.CharField(
        max_length=100,
        verbose_name="저자",
    )

    # AI·Wikipedia를 통해 생성하는 정보
    author_info = models.TextField(
        blank=True,
        verbose_name="작가 정보",
    )
    author_works = models.JSONField(
        default=list,
        blank=True,
        verbose_name="작가 대표 작품",
    )
    author_image_url = models.URLField(
        blank=True,
        verbose_name="작가 프로필 이미지",
    )

    def __str__(self):
        return self.title