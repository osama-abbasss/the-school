from django.contrib import admin
from .models import UserProfile, EmailConfirm


admin.site.register(UserProfile)
admin.site.register(EmailConfirm)
