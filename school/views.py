from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Lesson


def index(request):
    courses = Course.objects.order_by('-pub_date')[:5]
    context = {'courses': courses}
    return render(request, 'school/index.html', context)


def detail(request, course_name):
    course = Course.objects.get(name=course_name)
    lessons = Lesson.objects.filter(course=course_name)
    context = {'course': course, 'lessons': lessons}
    return render(request, 'school/detail.html', context)