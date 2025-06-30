from rest_framework import serializers
from .models import Employees, departments, courses, students


class EmployeesSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = "__all__"

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = departments
        fields = "__all__"

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = courses
        fields = "__all__"
