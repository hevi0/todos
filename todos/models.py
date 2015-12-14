from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Todos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

class TodoItem(models.Model):
    todos = models.ForeignKey('Todos', on_delete=models.CASCADE, related_name="todo_items")
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)