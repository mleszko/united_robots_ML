from django.db import models

# Create your models here.


class Robot(models.Model):
    """" Robot device data"""
    name = models.CharField


class Position(models.Model):
    """ Curent Robot position with datetime"""
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE)
    x = models.IntegerField
    y = models.IntegerField
    datetime = models.DateTimeField
