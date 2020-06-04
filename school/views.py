from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Lesson, Topic


def topics(request):
    topics = Topic.objects.order_by('-pub_date')[:5]
    context = {'topics': topics}
    return render(request, 'school/topics.html', context)


def courses(request, topic_name):
    topic = Topic.objects.get(name=topic_name)
    courses = Course.objects.filter(topic=topic)
    context = {'courses': courses}
    return render(request, 'school/courses.html', context)



def lessons(request, topic_name, course_name):
    course = Course.objects.get(name=course_name)
    lessons = Lesson.objects.filter(course=course)
    context = {'course': course, 'lessons': lessons, 'topic': course.topic}
    return render(request, 'school/lessons.html', context)

def details(request, topic_name, course_name, lesson_name):
    lesson = Lesson.objects.get(name=lesson_name)
    course = lesson.course
    context = {'course': course, 'lesson': lesson}
    return render(request, 'school/detail.html', context)