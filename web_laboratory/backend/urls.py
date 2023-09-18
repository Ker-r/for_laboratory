from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.ProjectView.as_view(), name='projects'),
    path('staff/', views.staff, name='staff'),
    # Просмотр записи
    path('projects/<int:post_pk>/', views.ProjectDetail.as_view(), name='project_detail'),
]
