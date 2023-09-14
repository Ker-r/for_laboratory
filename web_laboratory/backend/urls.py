from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('staff/', views.staff, name='staff'),
    # Просмотр записи
    path(
        'projects/<int:project_id>/',
        views.project_detail, name='project_detail'
    ),
]
