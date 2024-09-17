from django.db import models

class Video (models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='videos/thumbnails')
    source = models.FileField(upload_to='videos')