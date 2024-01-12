from django.db import models

# Create your models here.

## [id_task, task, done"True or False"]

class TaskList(models.Model):
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.task + "- Task |" + str(self.done)
    
    