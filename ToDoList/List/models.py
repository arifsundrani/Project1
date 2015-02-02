from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
<<<<<<< HEAD
	task_text = models.CharField(max_length=1000, unique=True)
=======
	task_text = models.TextField()#CharField(max_length=1000)
>>>>>>> FETCH_HEAD
	completed = models.BooleanField(default=False)
	def __str__(self):
		return self.task_text