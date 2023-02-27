from django.db import models

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=100)
	section = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	marks = models.FloatField()

	def __str__(self):
		return self.name