from django.urls import path
from .views import JobListView, JobDetailView, ApplyJobView

urlpatterns = [
    path('know/', JobListView.as_view(), name='job-list'),
    path('know/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('know/<int:job_id>/apply/', ApplyJobView.as_view(), name='apply-job'),
]
