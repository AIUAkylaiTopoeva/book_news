from rest_framework import generics 

from .models import New
from .serializers import NewSerializers

class NewList(generics.ListCreateAPIView): 
    queryset = New.objects.all() 
    serializer_class = NewSerializers

class NewDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = New.objects.all()
    serializer_class = NewSerializers