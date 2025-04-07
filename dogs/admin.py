from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Breed, Dog

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'group')
    search_fields = ('name',)

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'age', 'gender')
    list_filter = ('breed', 'gender')
    search_fields = ('name',)
