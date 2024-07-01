# jobs/admin.py
from django.contrib import admin
from .models import Job, Candidate

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'is_active', 'created_at')
    search_fields = ('title', 'location')
    list_filter = ('is_active', 'location')
    ordering = ('-created_at',)

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'applied_job', 'applied_at')
    search_fields = ('first_name', 'last_name', 'email', 'applied_job__title')
    list_filter = ('applied_job',)
    ordering = ('-applied_at',)
