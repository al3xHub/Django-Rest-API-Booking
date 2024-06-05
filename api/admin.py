from django.contrib import admin
from .models import Recursos, Reservas
from rest_framework.authtoken.admin import TokenAdmin

# Register your models here.
admin.site.register(Recursos)
admin.site.register(Reservas)
TokenAdmin.raw_id_fields=['user']

