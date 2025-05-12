# from django.urls import path
# from .views import TodoListCreateView, TodoRetrieveUpdateDestroyView, TaskListCreateView, TaskRetrieveUpdateDestroyView

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# urlpatterns = [

#     path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

#     path('api/todos', TodoListCreateView.as_view(), name='todo-list-create'),
#     path('api/todos/<int:pk>', TodoRetrieveUpdateDestroyView.as_view(), name='todo-detail'),

#     path('api/todos/<int:todo_id>/tasks', TaskListCreateView.as_view(), name='task-list-create'),
#     path('api/tasks/<int:pk>', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
# ]



from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import TodoListCreateView, TodoRetrieveUpdateDestroyView, TaskListCreateView, TaskRetrieveUpdateDestroyView, TaskListCreateView, ImageRetrieveUpdateDestroyView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/todos/', TodoListCreateView.as_view(), name='todo-list-create'),
    path('api/todos/<int:pk>/', TodoRetrieveUpdateDestroyView.as_view(), name='todo-detail'),
    path('api/todos/<int:todo_id>/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('api/tasks/<int:task_id>/images/', TaskListCreateView.as_view(), name='task-images-list-create'),
    path('api/images/<int:pk>/', ImageRetrieveUpdateDestroyView.as_view(), name='image-detail'),
]