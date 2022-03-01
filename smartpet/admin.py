from django.contrib import admin
from .models import petType, petBreed, Pet, petPhoto
# Register your models here.

admin.site.register(petType)


# Custom model Admin (admin.py):
# We can specify which database fields are visible in admin panel


class petBreedAdmin(admin.ModelAdmin):
    fields = ("name", "pettype")  # Fields to use for add/edit/show page
    list_display = ("name", "pettype")  # fields to display in search page
    # fields that will be a link in search page
    list_display_links = ("name", "pettype")


# Register app
admin.site.register(petBreed, petBreedAdmin)


class PetAdmin(admin.ModelAdmin):
    # Fields to use for add/edit/show page
    fields = ("name", "pettype", "petbreed", "owner")
    # fields to display in search page
    list_display = ("name", "pettype", "petbreed", "owner")
    # fields that will be a link in search page
    list_display_links = ("name", "pettype", "petbreed", "owner")


# Register app
admin.site.register(Pet, PetAdmin)


class photoAdmin(admin.ModelAdmin):
    fields = ("pet", "url")  # Fields to use for add/edit/show page
    list_display = ("pet", "url")  # fields to display in search page
    # fields that will be a link in search page
    list_display_links = ("pet", "url")


# Register app
admin.site.register(petPhoto, photoAdmin)
