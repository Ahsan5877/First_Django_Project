from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Employees , departments, students, courses
from .serializers import EmployeesSerialzers, DepartmentSerializers, StudentSerializers, CourseSerializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend   

class CustomPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'

class LimitOffsetCustomPagination(LimitOffsetPagination):
    default_limit = 3
    limit_query_param = 'limit'
    offset_query_param = 'offset'

class CursorCustomPagination(CursorPagination):
    page_size = 4
    ordering = 'stu_id'
    page_size_query_param = 'page_size'


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerialzers

class deparmentsViewSet(viewsets.ModelViewSet):
    queryset = departments.objects.all()
    serializer_class = DepartmentSerializers
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Depart_name']

class studentsViewSet(viewsets.ModelViewSet):
    queryset = students.objects.all()
    serializer_class = StudentSerializers
    pagination_class = CursorCustomPagination
    filter_backends = [SearchFilter]
    search_fields = ['stu_name', 'stu_city']
class coursesViewSet(viewsets.ModelViewSet):
    queryset = courses.objects.all()
    serializer_class = CourseSerializers
    pagination_class = LimitOffsetCustomPagination    
    filter_backends = [OrderingFilter]
    ordering = ['Course_id']


# class EmployeesViewSet(APIView):
#     def get(self, request, id=None): 
#         if id:
#             data = models.Employees.objects.get(id=id)
#             serializer = serializers.EmployeesSerialzers(data)
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
#         data = models.Employees.objects.all()
#         serializer = serializers.EmployeesSerialzers(data, many=True)
#         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = serializers.EmployeesSerialzers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#         return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
#     def patch(self, request, id= None):
#         data = models.Employees.objects.get(id=id)
#         serializer = serializers.EmployeesSerialzers(data, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "suceess", "data": serializer.data}, status=status.HTTP_200_OK)
#         else:
#             return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_200_OK)
    
#     def delete(self, request, id=None):
#         data = models.Employees.objects.filter(id=id)
#         data.delete()
#         return Response({"status": "success", "data": "Item Deleted"})






# class BaseViewSet(APIView):
#     model = None
#     serializer_class = None

#     def get(self, request, id=None):
#         if id:
#             data = self.model.objects.get(id=id)
#             serializer = self.serializer_class(data)
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
#         data = self.model.objects.all()
#         serializer = self.serializer_class(data, many=True)
#         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
#         return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
#     def patch(self, request, id=None):
#         data = self.model.objects.get(id=id)
#         serializer = self.serializer_class(data, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#         return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, id=None):
#         data = self.model.objects.filter(id=id)
#         if not data.exists():
#             return Response({"status": "error", "data": "Item not found"}, status=status.HTTP_404_NOT_FOUND)    
#         data.delete()
#         return Response({"status": "success", "data": "Item Deleted"}, status=status.HTTP_200_OK)
    
# class EmployeesViewSet(BaseViewSet):
#     model = Employees
#     serializer_class = EmployeesSerialzers

# class StudentsViewSet(BaseViewSet):
#     model = students
#     serializer_class = StudentSerializers

# class DepartmentsViewSet(BaseViewSet):
#     model = departments
#     serializer_class = DepartmentSerializers
# class CoursesViewSet(BaseViewSet):
#     model = courses
#     serializer_class = CourseSerializers