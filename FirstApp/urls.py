from django.urls import path
from . import views

urlpatterns = [
    path('FirstApp/', views.FirstApp, name='FirstApp'),
]