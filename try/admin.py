from django.contrib import admin

# Register your models here.
from .models import Contact, Direct

admin.site.register(Contact)
admin.site.register(Direct)