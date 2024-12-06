from rest_framework import serializers
from tutorials.models import *

class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial  # Change this if User model exists
        fields = ('login', 'pwd')
