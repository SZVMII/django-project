from django.db.models import ExpressionWrapper, FloatField, F
from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from rest_framework.response import Response
from .models import Part
from .serializer import PartSerializer, PartLocationFilterSerializer


class CreateView(generics.CreateAPIView):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user_added=self.request.user, )


class PartList(generics.ListAPIView):
    queryset = Part.objects.filter(status='zaakceptowane')
    serializer_class = PartSerializer

    def display(self):
        return super().get_queryset()
