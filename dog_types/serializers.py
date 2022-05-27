from rest_framework import serializers
from .models import Dog_type

class Dog_type_serializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'breed', 'description')
        model = Dog_type