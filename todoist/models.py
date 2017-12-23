from django.db import models
from datetime import datetime

class User(models.Model):
	"""用户模型"""
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=200)
	seen_time = models.DateField(auto_now_add=True)

		

class Task(models.Model):
	"""任务模型"""
	task_title = models.CharField(max_length=50)
	deta = models.TextField()
	timestamp = models.DateField(auto_now_add=True)
	user_id = models.ManyToManyField(User)