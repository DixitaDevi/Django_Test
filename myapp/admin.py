from django.contrib import admin

# Register your models here.
from .models import Notes, User
admin.site.register(Notes)
admin.site.register(User)
