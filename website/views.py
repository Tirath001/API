from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Services, industries, ARFeature, ARBenefit, ARCaseStudy, Home_CaseStudy, Home_services, Blogs
from .serializers import ServicesSerializer, industrieSerializer, ARFeatureSerializer, ARBenefitSerializer, ARCaseStudySerializer, Home_CaseStudySerializer, Home_Services_Serializer, Blog_Serializer

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    @action(detail=False, url_path='meta-tag/(?P<meta_tag>[^/.]+)', methods=['get'])
    def get_by_meta_tag(self, request, meta_tag=None):
        instance = get_object_or_404(Services, meta_tag=meta_tag)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class industriesViewSet(viewsets.ModelViewSet):
    queryset = industries.objects.all()
    serializer_class = industrieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    @action(detail=False, url_path='meta-tag/(?P<meta_tag>[^/.]+)', methods=['get'])
    def get_by_meta_tag(self, request, meta_tag=None):
        instance = get_object_or_404(industries, meta_tag=meta_tag)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class ARFeatureListView(viewsets.ModelViewSet):
    queryset = ARFeature.objects.all().order_by('title')
    serializer_class = ARFeatureSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    @action(detail=False, url_path='meta-tag/(?P<meta_tag>[^/.]+)', methods=['get'])
    def get_by_meta_tag(self, request, meta_tag=None):
        instance = get_object_or_404(ARFeature, meta_tag=meta_tag)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class ARBenefitListView(viewsets.ModelViewSet):
    queryset = ARBenefit.objects.all().order_by('title')
    serializer_class = ARBenefitSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    @action(detail=False, url_path='meta-tag/(?P<meta_tag>[^/.]+)', methods=['get'])
    def get_by_meta_tag(self, request, meta_tag=None):
        instance = get_object_or_404(ARBenefit, meta_tag=meta_tag)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class ARCaseStudyListView(viewsets.ModelViewSet):
    queryset = ARCaseStudy.objects.all().order_by('title')
    serializer_class = ARCaseStudySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    @action(detail=False, url_path='meta-tag/(?P<meta_tag>[^/.]+)', methods=['get'])
    def get_by_meta_tag(self, request, meta_tag=None):
        instance = get_object_or_404(ARCaseStudy, meta_tag=meta_tag)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class Home_CaseStudyListView(viewsets.ModelViewSet):
    queryset = Home_CaseStudy.objects.all().order_by('title')
    serializer_class = Home_CaseStudySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    @action(detail=False, url_path='meta-tag/(?P<meta_tag>[^/.]+)', methods=['get'])
    def get_by_meta_tag(self, request, meta_tag=None):
        instance = get_object_or_404(Home_CaseStudy, meta_tag=meta_tag)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class Home_services_ListView(viewsets.ModelViewSet):
    queryset = Home_services.objects.all().order_by('title')
    serializer_class = Home_Services_Serializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    @action(detail=False, url_path='meta-tag/(?P<meta_tag>[^/.]+)', methods=['get'])
    def get_by_meta_tag(self, request, meta_tag=None):
        instance = get_object_or_404(Home_services, meta_tag=meta_tag)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class Blog_ListView(viewsets.ModelViewSet):
    queryset = Blogs.objects.all().order_by('title')
    serializer_class = Blog_Serializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    @action(detail=False, url_path='meta-tag/(?P<meta_tag>[^/.]+)', methods=['get'])
    def get_by_meta_tag(self, request, meta_tag=None):
        instance = get_object_or_404(Blogs, meta_tag=meta_tag)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
