from django.contrib import admin
from .models import Blog, BlogAdmin

# Register your models here.
admin.site.register(Blog, BlogAdmin)