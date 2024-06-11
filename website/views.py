from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Services, industries
from .serializers import ServicesSerializer , industrieSerializer

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read for unauthenticated users, write for authenticated

class industriesViewSet(viewsets.ModelViewSet):
    queryset = industries.objects.all()
    serializer_class = industrieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 
