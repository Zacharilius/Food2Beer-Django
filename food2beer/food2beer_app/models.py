from django.db import models

class Brewery(models.Model):
	name = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)


	def __unicode__(self):
		return self.name
	
	class Meta:
		ordering = ["-name"]
