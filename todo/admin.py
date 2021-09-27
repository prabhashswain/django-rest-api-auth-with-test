from django.contrib import admin
from todo.models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title','description','author','created_at','updated_at']
    list_filter = ['title']