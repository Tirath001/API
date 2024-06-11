from rest_framework import serializers
from .models import Services , industries

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class industrieSerializer(serializers.ModelSerializer):
    class Meta:
        model = industries
        fields = '__all__'