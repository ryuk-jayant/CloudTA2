from django.contrib import admin

# Register your models here.
from .models import Task

class TaskAdminArea(admin.AdminSite):
    site_header="User login"

Taskadmin=TaskAdminArea(name="TaskAdmin")
Taskadmin.register(Task)
