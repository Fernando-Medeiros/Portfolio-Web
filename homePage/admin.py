from django.contrib import admin

from .models import Project, ProjectDetail, Stack

admin.site.register(Project)
admin.site.register(ProjectDetail)
admin.site.register(Stack)
