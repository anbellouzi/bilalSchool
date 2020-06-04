from django.contrib import admin

# Register your models here.
from .models import Course, Lesson, Topic

admin.site.register(Topic)
admin.site.register(Course)
admin.site.register(Lesson)

