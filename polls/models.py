from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=200)
    open = models.TimeField()
    start = models.TimeField()
    ticket = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title