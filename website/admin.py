from django.contrib import admin
from .models import Services , industries

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'detail', 'image')  
    search_fields = ('title', 'detail')  

@admin.register(industries)
class industriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'detail', 'image')  
    search_fields = ('title', 'detail')  