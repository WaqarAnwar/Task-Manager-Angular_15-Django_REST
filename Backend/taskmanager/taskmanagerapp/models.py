from django.db import models
import uuid

class Task(models.Model):
    id = models.CharField(max_length=90, blank=True, unique=True,primary_key=True, default=uuid.uuid4)
    task_name = models.CharField(max_length=200)
    complete=models.BooleanField()
    def __str__(self):
        return self.task_name