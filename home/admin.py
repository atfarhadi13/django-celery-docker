from django.contrib import admin

from .models import ExampleModel

@admin.register(ExampleModel)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
