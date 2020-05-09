from django.urls import path, include
from . import views

app_name = 'index'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('auth/', views.auth, name='auth')
]
