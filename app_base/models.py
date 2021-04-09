from django.db import models


class Employee(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    birthday = models.DateField()
    employment_date = models.DateField()

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Project(models.Model):
    acronym = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.acronym}'


class TimeSheet(models.Model):
    Q1 = 'Q1'
    Q2 = 'Q2'
    FORTNIGHT = [(Q1, 'Q1'), (Q2, 'Q2')]
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, related_name="timesheets", null=True)
    fortnight = models.CharField(max_length=2, choices=FORTNIGHT)
    month = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        unique_together = ('employee', 'fortnight', 'month', 'year')

    def __str__(self):
        return f'{self.employee.last_name[:3].upper()}' \
               f'{self.employee.first_name[:3].upper()}-' \
               f'{self.fortnight}{self.month}.{self.year} '


class TimeSheetDetail(models.Model):
    timesheet = models.ForeignKey(TimeSheet, related_name="timesheet_details", on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, related_name="timesheet_projects", on_delete=models.SET_NULL, null=True)
    hours = models.FloatField()

    class Meta:
        unique_together = ('timesheet', 'project')

    def __str__(self):
        return f'{self.timesheet}-{self.project}'
