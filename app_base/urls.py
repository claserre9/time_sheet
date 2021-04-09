from django.urls import path

from app_base import views

urlpatterns = [
    path('employees/', views.EmployeeList.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('timesheet/', views.TimeSheetList.as_view()),
    path('timesheet/<int:pk>/', views.TimeSheetDetail.as_view()),
]
