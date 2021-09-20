from django.db import models
from django.db.models import fields

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    api_id = models.CharField(max_length=255, null=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    authors = models.ManyToManyField(Author)
    published_date = models.PositiveSmallIntegerField(blank=False, null=True)
    categories = models.ManyToManyField(Category, blank=True)
    average_rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    ratings_count = models.PositiveSmallIntegerField(blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['api_id']),
            ]
    def __str__(self) -> str:
        return self.title
