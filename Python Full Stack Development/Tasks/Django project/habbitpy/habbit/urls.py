from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create/', views.create_habit, name='create_habit'),
    path('habit/<int:habit_id>/', views.habit_detail, name='habit_detail'),  # ← Add this line
    path('log/<int:habit_id>/', views.log_habit, name='log_habit'),
    path('logs/<int:habit_id>/', views.view_logs, name='view_logs'),
    path('register/', views.register, name='register'),
]