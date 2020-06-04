from django.db import models
import datetime
from django.utils import timezone


class Topic(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200, null=True, default=None)
    description = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published', default=None)

    # votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Course(models.Model):
    name = models.CharField(max_length=200)
    topic =  models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    image = models.CharField(max_length=200, null=True, default=None)

    def __str__(self):
        return self.name
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Lesson(models.Model):
    name = models.CharField(max_length=200)
    course =  models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    video = models.CharField(max_length=200)
    image = models.CharField(max_length=200, null=True, default=None)
    description = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published', default=None)

    # votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

