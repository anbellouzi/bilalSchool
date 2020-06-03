from django.urls import path

from . import views

app_name = 'school' 

urlpatterns = [
    path('', views.index, name='index'),
    path('course/<str:course_name>/', views.detail, name='detail'),
]