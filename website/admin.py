from django.contrib import admin
from .models import Services , industries , ARFeature, ARBenefit, ARCaseStudy, Home_CaseStudy, Home_services, Blogs

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','image','meta_tag')  
    search_fields = ('title',)  

@admin.register(industries)
class industriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image','meta_tag')  
    search_fields = ('title',)  
@admin.register(ARFeature)
class ARFeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image','meta_tag')
    search_fields = ('title',)

@admin.register(ARBenefit)
class ARBenefitAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image','meta_tag')
    search_fields = ('title',)

@admin.register(ARCaseStudy)
class ARCaseStudyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image','meta_tag')
    search_fields = ('title',)

@admin.register(Home_CaseStudy)
class HomeCaseStudyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image','meta_tag')
    search_fields = ('title',)

@admin.register(Home_services)
class Home_services_StudyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image','float_icon','meta_tag')
    search_fields = ('title',)

@admin.register(Blogs)
class Blogs_StudyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image','meta_tag')
    search_fields = ('title',)