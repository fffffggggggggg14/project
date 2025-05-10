from django.shortcuts import render

from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

class TodoListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id']
    search_fields = ['title']

class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

##
##