from django.contrib import admin
from .models import Student, Homework

admin.site.register([Student,Homework])
