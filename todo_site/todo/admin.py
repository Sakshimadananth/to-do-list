from django.contrib import admin # type: ignore
from .models import Todo
# Register your models here.
admin.site.register(Todo)