from django.shortcuts import render
from .models import TaskList
# Create your views here.

def todolist(request):
    all_tasks = TaskList.objects.all()
    return render(request, 'todolist.html',{'all_tasks':all_tasks})

def contactus(request):
    content = {
        'todo_from' : 'Welcome to Contact Page'
    }
    return render(request, 'todolist.html',content)

def aboutus(request):
    content = {
        'todo_from' : 'Welcome to About Page'
    }
    return render(request, 'todolist.html',content)