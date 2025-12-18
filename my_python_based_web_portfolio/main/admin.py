from django.contrib import admin
from .models import WorkImage


@admin.register(WorkImage)
class WorkImageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'uploaded_at')
