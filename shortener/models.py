from django.db import models

# Create your models here.
class ShortenUrl(models.Model):
    url = models.URLField()
    short_url = models.CharField(max_length=255, primary_key=True)
    add_date = models.DateTimeField()

    def __str__(self):
        return self.url
