from django.contrib import admin
from records.models import Blog

# Register your models here.
@admin.register(Blog)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'name_slug', 'desc', 'is_active',]