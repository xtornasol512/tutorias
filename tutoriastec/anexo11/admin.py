from django.contrib import admin
from .models import OrganizacionEstudio, MotivacionEstudio, TecnicasEstudio, InventarioEstudio

# Register your models here.
admin.site.register(OrganizacionEstudio)
admin.site.register(MotivacionEstudio)
admin.site.register(TecnicasEstudio)
admin.site.register(InventarioEstudio)