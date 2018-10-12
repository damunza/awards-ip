from rest_framework import serializers
from .models import Project, Profile

class Profileserializer(serializers.ModelSerializer):
    class Meta:
        models = Profile
        fields = ('name','bio','contact')
