from django.contrib import admin

# Register your models here.
from app_base import models
from app_base.models import TimeSheet, TimeSheetDetail


class TimeSheetDetailsInline(admin.TabularInline):
    model = TimeSheetDetail


class TimeSheetAdmin(admin.ModelAdmin):
    inlines = [TimeSheetDetailsInline]

    class Meta:
        model = TimeSheet


admin.site.register(models.TimeSheet, TimeSheetAdmin)

admin.site.register(models.Project)
admin.site.register(models.Employee)

# admin.site.register(models.TimeSheetDetail)
