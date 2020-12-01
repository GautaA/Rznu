from django.shortcuts import render
from rest_framework import viewsets

from .serializers import BandSerializer
from .models import Band

class BandViewSet(viewsets.ModelViewSet):
	queryset = Band.objects.all().order_by('name')
	serializer_class = BandSerializer