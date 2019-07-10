from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CollectionSerializer
from .models import Collection

# Create your views here.


class CollectionView(viewsets.ModelViewSet):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
