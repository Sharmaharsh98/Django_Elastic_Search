from django.contrib import admin
from .models import Alphabets

# Register your models here.
@admin.register(Alphabets)
class AlphaAdmin(admin.ModelAdmin):
    fields = ['alphabet', 'word']