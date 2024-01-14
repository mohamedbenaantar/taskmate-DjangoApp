from django import forms
from todolist_app.models import TaskList

## which database I'm connecting to 

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['task', 'done'] ## mention the fields that I'm going to edit
        
    