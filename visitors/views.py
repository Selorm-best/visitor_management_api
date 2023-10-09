from django.shortcuts import render
from rest_framework import generics
from .models import Visitor, Visit, Destination
from .serializers import VisitorSerializer,VisitSerializer, DestinationSerializer

class VistorListCreateView(generics.ListCreateAPIView):
    queryset=Visitor.objects.all()
    serializer_class = VisitorSerializer

class VisitListCreateView(generics.ListCreateAPIView):
    queryset=Visit.objects.all()
    serializer_class = VisitSerializer

class DestinationListCreateView(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

# Create your views here.
