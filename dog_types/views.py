from rest_framework import generics
from .models import Dog_type
from .serializers import Dog_type_serializer

class Dog_type_list(generics.ListCreateAPIView):
    queryset = Dog_type.objects.all()
    serializer_class = Dog_type_serializer

class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog_type.objects.all()
    serializer_class = Dog_type_serializer
