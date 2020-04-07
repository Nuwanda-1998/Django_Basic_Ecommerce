from django.contrib import admin
from .models import UserProfileInfo, PCategory, Products
# Register your models here.

admin.site.register(UserProfileInfo)
admin.site.register(PCategory)
admin.site.register(Products)