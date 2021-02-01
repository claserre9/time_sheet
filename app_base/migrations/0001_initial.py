# Generated by Django 3.1.5 on 2021-02-01 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('birthday', models.DateField()),
                ('employment_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acronym', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fortnight', models.CharField(choices=[('Q1', 'Q1'), ('Q2', 'Q2')], max_length=2)),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_base.employee')),
            ],
            options={
                'unique_together': {('employee', 'fortnight', 'month', 'year')},
            },
        ),
        migrations.CreateModel(
            name='TimeSheetDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.FloatField()),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_base.project')),
                ('timesheet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_base.timesheet')),
            ],
            options={
                'unique_together': {('timesheet', 'project')},
            },
        ),
    ]
