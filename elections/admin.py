from django.contrib import admin
from elections.models import Election

# Register your models here.
@admin.register(Election)
class ElectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'year', 'name']
    list_filter = ['year', 'name']
    search_fields = ['name']