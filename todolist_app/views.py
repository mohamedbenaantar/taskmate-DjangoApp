from django.shortcuts import render, redirect
from .models import TaskList
from .forms import TaskForm
from django.contrib import messages
# Create your views here.

def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, 'Task Added successfully!')
        return redirect('todolist') 
    else: ## Get request
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