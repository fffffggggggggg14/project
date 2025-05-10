from django.shortcuts import render

from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import filters

class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id']
    search_fields = ['title']

class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

