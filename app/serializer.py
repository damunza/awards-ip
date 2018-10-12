from rest_framework import serializers
from .models import Project, Profile

class Profileserializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name','bio','contact')

class Projectserializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('by','title','description','link')
