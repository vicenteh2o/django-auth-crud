from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('title', 'user', 'created', 'datecompleted', 'important')
    search_fields = ('title', 'user__username')
    list_filter = ('important', 'created')


# Register your models here.
admin.site.register(Task, TaskAdmin)
