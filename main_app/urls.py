from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('process_uploaded_files/', views.process_uploaded_files, name='process_uploaded_files'),
]
