from django.urls import path
from .views import ContactInformationView, ContactFormSubmissionView
urlpatterns = [
    path('contact-info/', ContactInformationView.as_view(), name='contact-info'),
    path('submit-form/', ContactFormSubmissionView.as_view(), name='submit-form'),
]
