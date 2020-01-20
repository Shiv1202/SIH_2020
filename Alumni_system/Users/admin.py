from django.contrib import admin
from .models import Colleges, Alumni_User,Permanent_User

# Register your models here.
admin.site.register(Colleges)
admin.site.register(Alumni_User)
admin.site.register(Permanent_User)