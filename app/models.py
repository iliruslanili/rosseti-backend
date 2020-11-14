from django.db import models


# Create your models here.
# class SystemExchangeDescription(models.Model):
#     pass

class Validators(models.Model):
    name = models.CharField(max_length=200)


class Attributes(models.Model):
    name = models.CharField(max_length=100)
    validator = models.ForeignKey(Validators, on_delete=models.CASCADE)


class DeviceType(models.Model):
    name = models.CharField(max_length=200)


class Device(models.Model):
    name = models.CharField(max_length=120)
    type = models.ForeignKey(DeviceType, on_delete=models.DO_NOTHING)
    attributes = models.ManyToManyField(Attributes)
