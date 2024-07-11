# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServicesViewSet, industriesViewSet, ARFeatureListView, ARBenefitListView, ARCaseStudyListView, Home_CaseStudyListView, Home_services_ListView, Blog_ListView

router = DefaultRouter()
router.register(r'services', ServicesViewSet, basename='services')
router.register(r'industries', industriesViewSet, basename='industries')
router.register(r'ar-features', ARFeatureListView, basename='ar-features-list')
router.register(r'ar-benefits', ARBenefitListView, basename='ar-benefits-list')
router.register(r'ar-case-studies', ARCaseStudyListView, basename='ar-case-studies-list')
router.register(r'home-case-studies', Home_CaseStudyListView, basename='Home-case-studies-list')
router.register(r'services-list', Home_services_ListView, basename='Home-services')
router.register(r'blog', Blog_ListView, basename='blogs')

urlpatterns = [
    path('web/', include(router.urls)),
]
