from rest_framework import serializers
from .models import ContactInformation, ContactFormSubmission

class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = ['address', 'phone', 'email']

class ContactFormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactFormSubmission
        fields = ['name', 'email', 'subject', 'message', 'attachment']
