from django.contrib import admin
from .models import Firma

# Register your models here.
class AdminFirma(admin.ModelAdmin):
    list_display = ["nombre", "gid", "departamento", "posicion", "dispositivo","detalles", "firma"]

admin.site.register(Firma, AdminFirma)