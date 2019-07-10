from django.db import models

# Create your models here.


class Collection(models.Model):
    title = models.CharField(max_length=48)
    animation_speed = models.FloatField(default=0.5)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
