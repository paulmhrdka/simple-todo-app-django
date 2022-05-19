from django.contrib import admin
from .models import Todo

# Register your models here.
class TodosAdmin(admin.ModelAdmin):
    readonly_fields = [
        'created',
        'completed',
    ]

admin.site.register(Todo, TodosAdmin)