from django.shortcuts import render,redirect
from . models import Task
# Create your views here.
def Hello(request):
    name="jayant"
    return render(request,"Task/hello.html",{"info":name})

def Tasklist(request):
    if(str(request.user)!="AnonymousUser"):
        Tasks=Task.objects.filter(Person=request.user).order_by('T_priority')
        return render(request,"Task/list.html",{'bool':True,'tasks':Tasks,'user':request.user})
    else:
        Tasks=[{}]
        return render(request,"Task/list.html",{'bool':False,'tasks':Tasks})

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
    task=Task.objects.get(pk=pk)
    task.delete()
    print(task)
    return redirect('task list')