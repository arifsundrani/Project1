from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
	task_text = models.TextField()
	completed = models.BooleanField(default=False)
	def __str__(self):
		return self.task_text