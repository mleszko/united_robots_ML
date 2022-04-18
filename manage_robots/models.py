from datetime import datetime
from django.db import models

# Create your models here.


class Robot(models.Model):
    """ " Robot device data"""

    name = models.CharField(editable=True, max_length=128, default="")


class Position(models.Model):
    """Current Robot position with datetime"""

    robot = models.ForeignKey(Robot, on_delete=models.CASCADE)
    x = models.IntegerField(editable=True, default=0)
    y = models.IntegerField(editable=True, default=0)
    datetime = models.DateTimeField(editable=True, default=datetime.now())
