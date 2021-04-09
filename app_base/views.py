
from rest_framework import generics, permissions


from app_base.models import Employee, Project, TimeSheet
from app_base.serializers import EmployeeSerializer, ProjectSerializer, TimeSheetSerializer


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TimeSheetList(generics.ListCreateAPIView):
    queryset = TimeSheet.objects.all()
    serializer_class = TimeSheetSerializer


class TimeSheetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeSheet.objects.all()
    serializer_class = TimeSheetSerializer
