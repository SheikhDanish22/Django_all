from django.contrib import admin

# Register your models here.
from .models import (Department,Student)

admin.site.register(Department)
admin.site.register(Student)