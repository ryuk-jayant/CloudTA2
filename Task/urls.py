from django.contrib import admin
from django.urls import path,include
from . import views
from .admin import Taskadmin
urlpatterns = [
    path("Hello",views.Hello,name="Hello_view"),
    path("login",Taskadmin.urls),
    path("",views.Tasklist,name="task list"),
    path("add",views.add_task,name="add task"),
    path("done_task/<int:pk>",views.done_task,name="done_task")
]