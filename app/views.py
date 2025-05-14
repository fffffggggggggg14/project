from django.shortcuts import render
from rest_framework import generics
from .models import Todo, Task, Image
from .serializers import TodoSerializer, TaskSerializer, ImageSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import ValidationError

class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    ordering_fields = ['id']
    search_fields = ['title']

class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

#################################################################################################

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        todo_id = self.kwargs['todo_id']
        return Task.objects.filter(todo_id=todo_id)

    def perform_create(self, serializer):
        todo_id = self.kwargs['todo_id']
        try:
            todo = Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            raise ValidationError({"error": f"Todo with id {todo_id} does not exist."})
        serializer.save(todo_id=todo_id)



class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return Task.objects.all()


#################################################################################################


class ImageListView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

class ImageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]