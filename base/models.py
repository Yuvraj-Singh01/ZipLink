from django.db import models

# Create your models here.

class ShortenedURL(models.Model):
    original_url = models.URLField(unique=True)
    shortened_id = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.original_url} -> {self.shortened_id}"