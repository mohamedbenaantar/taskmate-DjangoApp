from django.shortcuts import render

# Create your views here.

def todolist(request):
    content = {
        'todo_from' : 'todoList Template'
    }
    return render(request, 'todolist.html',content)

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