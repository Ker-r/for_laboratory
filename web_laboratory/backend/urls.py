from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.ProjectView.as_view(), name='projects'),
    path('staff/', views.StaffView.as_view(), name='staff'),
    path('projects/<int:post_pk>/', views.ProjectDetail.as_view(), name='project_detail'),
    path('staff/<int:post_pk>/', views.StaffDetail.as_view(), name='staff_detail'),
]
