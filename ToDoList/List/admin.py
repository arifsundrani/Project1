from django.contrib import admin
from List.models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
	list_display = ["task_text","completed"]

admin.site.register(Task, TaskAdmin)
