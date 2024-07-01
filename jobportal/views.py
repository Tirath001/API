from rest_framework import generics
from .models import Job, Candidate
from .serializers import JobSerializer, CandidateSerializer
from .pagination import JobListPagination
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter

class JobFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    location = filters.CharFilter(field_name='location', lookup_expr='icontains')

    class Meta:
        model = Job
        fields = ['title', 'location']

class JobListView(generics.ListAPIView):
    queryset = Job.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = JobSerializer
    pagination_class = JobListPagination
    filter_backends = [filters.DjangoFilterBackend, SearchFilter]
    filterset_class = JobFilter
    search_fields = ['title', 'location']

class JobDetailView(generics.RetrieveAPIView):
    queryset = Job.objects.filter(is_active=True)
    serializer_class = JobSerializer

class ApplyJobView(generics.CreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
