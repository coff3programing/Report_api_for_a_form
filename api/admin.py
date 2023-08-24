from django.contrib import admin
from .models import Parroquia, Sector, Barrio, Direccion, Usuario

# Register your models here.
admin.site.register(Parroquia)
admin.site.register(Sector)
admin.site.register(Barrio)
admin.site.register(Direccion)
admin.site.register(Usuario)