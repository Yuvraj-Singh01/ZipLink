from django.db import models

# Create your models here.
class short_urls(models.Model):
    original_link = models.CharField(max_length = 2000)
    shortened_link = models.CharField(max_length = 50)
    