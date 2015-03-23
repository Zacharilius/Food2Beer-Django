from django.db import models
from django.template.defaultfilters import slugify
class Brewery(models.Model):
	name = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	slug = models.SlugField(max_length=40, unique=True)

	def get_absolute_url(self):
		return self.slug

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Brewery, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name
	
	class Meta:
		ordering = ["-name"]
