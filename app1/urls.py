from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name= 'index'),
    path('register/', views.register, name= 'register'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('meeting/',views.videocall, name='meeting'),
    path('join/',views.join_room, name='join_room'),
    path('login/', views.user_login, name= 'login'),
    path('logout/',views.user_logout, name='logout'),
]
