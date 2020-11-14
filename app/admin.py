from django.contrib import admin
from app import models
# Register your models here.

admin.site.register(models.Device)
admin.site.register(models.DeviceType)
admin.site.register(models.Attributes)
admin.site.register(models.Validators)