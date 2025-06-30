from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeesViewSet, deparmentsViewSet,coursesViewSet,studentsViewSet

router = DefaultRouter()
router.register(r'Employees', EmployeesViewSet)
router.register(r'departments', deparmentsViewSet)
router.register(r'students', studentsViewSet)
router.register(r'courses', coursesViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

# urlpatterns = [
#     path('api/Employees/', EmployeesViewSet.as_view()),
#     path('api/Employees/<int:id>/', EmployeesViewSet.as_view()),
#     path('api/departments/', DepartmentsViewSet.as_view()),
#     path('api/departments/<int:id>/', DepartmentsViewSet.as_view()),
#     path('api/students/', StudentsViewSet.as_view()),
#     path('api/students/<int:id>/', StudentsViewSet.as_view()),
#     path('api/courses/', CoursesViewSet.as_view()),
#     path('api/courses/<int:id>/', CoursesViewSet.as_view()),
# ]
