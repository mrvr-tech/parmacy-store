from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import StoreItem, LabRequest, User

admin.site.register(StoreItem)
admin.site.register(LabRequest)
admin.site.register(User, BaseUserAdmin)
