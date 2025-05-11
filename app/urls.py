from django.urls import path
from .views import TodoListCreateView, TodoRetrieveUpdateDestroyView, TaskListCreateView, TaskRetrieveUpdateDestroyView

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/todos/<int:todo_id>/tasks', TaskListCreateView.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
]

