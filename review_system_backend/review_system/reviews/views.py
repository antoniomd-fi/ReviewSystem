from django.shortcuts import render

from rest_framework import viewsets
from .models import Business, Review
from .serializers import BusinessSerializer, ReviewSerializer

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
