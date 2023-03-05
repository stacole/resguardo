from django.contrib import admin
from .models import Signature

# Register your models here.
class AdminSignature(admin.ModelAdmin):
    list_display = ["nombre", "gid", "departamento", "posicion", "dispositivo","detalles", "firma"]

admin.site.register(Signature, AdminSignature)