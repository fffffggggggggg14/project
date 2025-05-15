# from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from .views import TodoListCreateView, TodoRetrieveUpdateDestroyView, TaskListCreateView, TaskRetrieveUpdateDestroyView, ImageListView, ImageRetrieveUpdateDestroyView


# urlpatterns = [
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

#     path('todos/', TodoListCreateView.as_view(), name='todo-list-create'),
#     path('todos/<int:pk>/', TodoRetrieveUpdateDestroyView.as_view(), name='todo-detail'),

#     path('todos/<int:todo_id>/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
#     path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),

#     path('images/', ImageListView.as_view(), name='image-list-create'),
#     path('images/<int:pk>/', ImageRetrieveUpdateDestroyView.as_view(), name='image-detail'),
# ]





from django.urls import path
from .views import TodoListCreateView, TodoRetrieveUpdateDestroyView, TaskListCreateView, TaskRetrieveUpdateDestroyView, ImageListView, ImageRetrieveUpdateDestroyView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version='v1',
        description="API description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    )

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('todos/', TodoListCreateView.as_view(), name='todo_list_create'),
    path('todos/<int:pk>/', TodoRetrieveUpdateDestroyView.as_view(), name='todo_detail'),
    
    path('todos/<int:todo_id>/tasks/', TaskListCreateView.as_view(), name='task_list_create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task_detail'),
    
    path('images/', ImageListView.as_view(), name='image_list_create'),
    path('images/<int:pk>/', ImageRetrieveUpdateDestroyView.as_view(), name='image_detail'),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]




