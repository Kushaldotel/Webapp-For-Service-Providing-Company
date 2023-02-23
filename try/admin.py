from django.contrib import admin

# Register your models here.
from .models import Contact, Direct,Blog

admin.site.register(Contact)
admin.site.register(Direct)
admin.site.register(Blog)
