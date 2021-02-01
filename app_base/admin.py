from django.contrib import admin

# Register your models here.
from app_base import models

admin.site.register(models.Project)
admin.site.register(models.Employee)
admin.site.register(models.TimeSheet)
admin.site.register(models.TimeSheetDetail)
