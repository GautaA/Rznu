from django.db import models

class Band(models.Model):
	name = models.CharField(max_length = 30)
	genre = models.CharField(max_length = 15)

	def __str__(self):
		return self.name
		
