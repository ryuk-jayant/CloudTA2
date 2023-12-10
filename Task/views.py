from django.shortcuts import render,redirect
from . models import Task
# Create your views here.
def Hello(request):
    name="jayant"
    return render(request,"Task/hello.html",{"info":name})

def Tasklist(request):
    Tasks=Task.objects.filter(Person=request.user).order_by('T_priority')
    return render(request,"Task/list.html",{'tasks':Tasks,'user':request.user})

def add_task(request):
    if request.method=="POST":
        task=request.POST
        Task.objects.create(
            Person=request.user,
            T_name=task['t_name'],
            T_desc=task['t_description'],
            T_priority=task['priority']
        )
        return redirect('task list')
    return render(request,"Task/add_task.html",{})

def done_task(request,pk):
    print(pk)
    return redirect('task list')