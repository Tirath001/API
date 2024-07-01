from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Services, industries, ARFeature, ARBenefit, ARCaseStudy, Home_CaseStudy, Home_services, Blogs
from .serializers import ServicesSerializer , industrieSerializer ,  ARFeatureSerializer, ARBenefitSerializer, ARCaseStudySerializer, Home_CaseStudySerializer, Home_Services_Serializer, Blog_Serializer
from jobportal.pagination import JobListPagination 

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  

class industriesViewSet(viewsets.ModelViewSet):
    queryset = industries.objects.all()
    serializer_class = industrieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 

class ARFeatureListView(viewsets.ModelViewSet):
    queryset = ARFeature.objects.all().order_by('title')
    serializer_class = ARFeatureSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 

class ARBenefitListView(viewsets.ModelViewSet):
    queryset = ARBenefit.objects.all().order_by('title')
    serializer_class = ARBenefitSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ARCaseStudyListView(viewsets.ModelViewSet):
    queryset = ARCaseStudy.objects.all().order_by('title')
    serializer_class = ARCaseStudySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class Home_CaseStudyListView(viewsets.ModelViewSet):
    queryset = Home_CaseStudy.objects.all().order_by('title')
    serializer_class = Home_CaseStudySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class Home_services_ListView(viewsets.ModelViewSet):
    queryset = Home_services.objects.all().order_by('title')
    serializer_class = Home_Services_Serializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class Blog_ListView(viewsets.ModelViewSet):
    queryset = Blogs.objects.all().order_by('title')
    serializer_class = Blog_Serializer
    permission_classes = [IsAuthenticatedOrReadOnly]