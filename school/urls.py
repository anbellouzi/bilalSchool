from django.urls import path

from . import views

app_name = 'school' 

urlpatterns = [
    path('', views.topics, name='topics'),
    path('t/<str:topic_name>/courses', views.courses, name='courses'),
    path('t/<str:topic_name>/<str:course_name>/lessons/', views.lessons, name='lessons'),
    path('t/<str:topic_name>/<str:course_name>/<str:lesson_name>/', views.details, name='lesson_detail'),
    
]