__author__ = 'rrmerugu'

from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('project_id',)


admin.site.register(Project, ProjectAdmin)
