from django.contrib import admin
from . import models

admin.site.register(models.CommonData)
admin.site.register(models.LaunchData)

