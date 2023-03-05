from inspect import signature
from django.db import models

# Create your models here.



class Signature(models.Model):
	class Meta:
		verbose_name_plural = 'resguardos'
	nombre = models.CharField(max_length=32, blank=True, null=True)
	gid = models.CharField(max_length=50, blank=True, null=True)
	departamento = models.CharField(max_length=20, blank=True, null=True)
	posicion = models.CharField(max_length=50, blank=True, null=True)
	dispositivo = models.CharField(max_length=50, blank=True, null=True)
	detalles = models.CharField(max_length=50, blank=True, null=True)
	signature = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):

		return str(self.name)