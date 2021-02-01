from django.contrib import admin


from app_base import models
from app_base.models import TimeSheet, TimeSheetDetail, Project


class TimeSheetDetailsInline(admin.TabularInline):
    model = TimeSheetDetail


class TimeSheetAdmin(admin.ModelAdmin):
    list_display = ('employee', 'fortnight', 'month', 'year')
    list_filter = ('fortnight', 'month', 'year')
    search_fields = ['employee__last_name', 'employee__first_name', ]
    inlines = [TimeSheetDetailsInline]

    class Meta:
        model = TimeSheet


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('acronym', 'name', 'is_active')

    class Meta:
        model = Project


admin.site.register(models.TimeSheet, TimeSheetAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Employee)

# admin.site.register(models.TimeSheetDetail)
