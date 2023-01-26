from django.shortcuts import render, redirect
from .models import Task

# Create your views here.

def list_tasks(request):
    task = Task.objects.all()
    return render(request, 'list_tasks.html', {"task": task  })

def create_task(resquest):
    task = Task(title=resquest.POST['title'], description=resquest.POST['description'])
    task.save()
    return redirect('/task/')

def delete_task(request, task_id):
    delete = Task.objects.get(id=task_id)
    delete.delete()
    return redirect('/task/')