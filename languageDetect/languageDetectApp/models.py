from django.db import models

# Create your models here.

class languageDetect(models.Model):
    language = models.CharField(max_length=255)
    confidence = models.FloatField(default=0)
    reliable = models.BooleanField()