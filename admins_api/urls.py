from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CustomAdminListCreateView, CustomAdminRetrieveUpdateDestroyView

urlpatterns = [
    path('api/admins/', CustomAdminListCreateView.as_view(), name='admin-list-create'),
    path('api/admins/<int:pk>/', CustomAdminRetrieveUpdateDestroyView.as_view(), name='admin-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
