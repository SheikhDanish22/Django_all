from django.contrib import admin

# Register your models here.
from .models import (Vehical,Fuel)

admin.site.register(Vehical)
admin.site.register(Fuel)