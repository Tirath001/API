from rest_framework import serializers
from .models import Services , industries, ARFeature, ARBenefit, ARCaseStudy, Home_CaseStudy, Home_services, Blogs

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class industrieSerializer(serializers.ModelSerializer):
    class Meta:
        model = industries
        fields = '__all__'

class ARFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ARFeature
        fields = '__all__'  

class ARBenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ARBenefit
        fields = '__all__'

class ARCaseStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = ARCaseStudy
        fields = '__all__'

class Home_CaseStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Home_CaseStudy
        fields = '__all__'

class Home_Services_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Home_services
        fields = '__all__'

class Blog_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'