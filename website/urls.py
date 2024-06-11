from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServicesViewSet , industriesViewSet

router = DefaultRouter()
router.register(r'services', ServicesViewSet, basename='services')
router.register(r'industries', industriesViewSet, basename='industries')
urlpatterns = [
    path('web/', include(router.urls)),
]
