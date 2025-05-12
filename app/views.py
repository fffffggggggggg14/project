from django.shortcuts import render

from rest_framework import generics
from .models import Todo, Task
from .serializers import TodoSerializer, TaskSerializer
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Image
from .serializers import ImageSerializer

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


#########################################################################################

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        todo_id = self.kwargs['todo_id']
        return Task.objects.filter(todo_id=todo_id)

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


##########################################################################################


class ImageListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser, FormParser]

class ImageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser, FormParser]
