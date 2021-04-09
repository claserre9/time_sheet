from rest_framework import serializers

from app_base.models import Employee, Project, TimeSheet, TimeSheetDetail


class TimeSheetDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSheetDetail
        fields = '__all__'


class TimeSheetSerializer(serializers.ModelSerializer):
    timesheet_details = TimeSheetDetailSerializer(many=True, read_only=True)

    class Meta:
        model = TimeSheet
        fields = ("employee", "fortnight", "month", "year", "timesheet_details")


class EmployeeSerializer(serializers.ModelSerializer):
    timesheets = TimeSheetSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'phone', 'birthday', 'employment_date', 'timesheets')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
