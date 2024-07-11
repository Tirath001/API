from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ContactFormSubmission, ContactInformation
from .serializers import ContactFormSubmissionSerializer

class ContactFormSubmissionView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactFormSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Send email logic here
            return Response({'success': 'Message sent successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactInformationView(APIView):
    def get(self, request, *args, **kwargs):
        contact_info = ContactInformation.objects.first()
        if contact_info:
            data = {
                'address': contact_info.address,
                'phone': contact_info.phone,
                'email': contact_info.email,
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response({'error': 'Contact information not found'}, status=status.HTTP_404_NOT_FOUND)
