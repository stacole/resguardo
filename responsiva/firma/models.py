from inspect import signature
from django.db import models
from jsignature.fields import JSignatureField

# Create your models here.



class Firma(models.Model):
	class Meta:
		verbose_name_plural = 'resguardos'
	nombre = models.CharField(max_length=32, blank=True, null=True)
	gid = models.CharField(max_length=50, blank=True, null=True)
	departamento = models.CharField(max_length=20, blank=True, null=True)
	posicion = models.CharField(max_length=50, blank=True, null=True)
	dispositivo = models.CharField(max_length=50, blank=True, null=True)
	detalles = models.CharField(max_length=50, blank=True, null=True)
	firma = JSignatureField(blank=True, null=True)

	def __str__(self):

		return str(self.name)
	