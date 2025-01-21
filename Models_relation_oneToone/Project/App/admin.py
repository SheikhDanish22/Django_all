from django.contrib import admin

# Register your models here.
from .models import (Aadhar,Userprofile)

admin.site.register(Aadhar)
admin.site.register(Userprofile)