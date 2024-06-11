from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, EmployeeProfile, Attendance, Salary, Project, Leave

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # List display shows fields in the user list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    # Fields to filter by in the list view
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    # Fieldsets for adding or changing a user
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # Fields for adding a user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)

@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'educational_background', 'work_experience')
    search_fields = ('user__username', 'user__email', 'educational_background', 'work_experience')
    ordering = ('user',)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'status')
    list_filter = ('status', 'date')
    search_fields = ('employee__username', 'employee__email', 'date')
    ordering = ('-date',)

@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'amount', 'date')
    list_filter = ('date',)
    search_fields = ('employee__username', 'employee__email')
    ordering = ('-date',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ('name',)

@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ('employee', 'start_date', 'end_date', 'reason', 'status')
    list_filter = ('status', 'start_date', 'end_date')
    search_fields = ('employee__username', 'employee__email', 'reason')
    ordering = ('-start_date',)
