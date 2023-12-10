from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Task(models.Model):
    Person=models.ForeignKey(User,on_delete=models.CASCADE);
    T_name=models.CharField(max_length=30, null=False)
    T_desc=models.TextField(default="TASK IS ADDED ON "+str(date.today()))
    T_priority = models.CharField(max_length=10,default="Low")
    def publish(self):
        self.save()

    def __str__(self):
        return self.T_name

