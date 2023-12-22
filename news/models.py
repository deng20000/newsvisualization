from django.db import models
from mongoengine import *

from djongo import models

class News(models.Model):
    _id = models.ObjectIdField()
    new_date = models.CharField(max_length=255)
    new_deputy_title = models.CharField(max_length=255)
    new_image = models.CharField(max_length=255)
    new_link = models.CharField(max_length=255)
    new_title = models.CharField(max_length=255)

    class Meta:
        db_table = 'scrapy_data'


# Create your models here.
class NewsArticle(models.Model):
    source_id = models.CharField(max_length=100, null=True)
    source_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    url_to_image = models.URLField(null=True)
    published_at = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "News Article"
        verbose_name_plural = "News Articles"
        ordering = ['-published_at']



