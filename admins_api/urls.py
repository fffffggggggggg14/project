from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import  CustomAdminListCreateView, CustomAdminRetrieveUpdateDestroyView, RegisterView, PasswordResetRequestView, PasswordResetConfirmView

urlpatterns = [
    path('api/admins/', CustomAdminListCreateView.as_view(), name='admin-list-create'),
    path('api/admins/<int:pk>/', CustomAdminRetrieveUpdateDestroyView.as_view(), name='admin-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='user_register'),
    path('api/password_reset/', PasswordResetRequestView.as_view(), name='password_reset_request'),
    path('api/password_reset/confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]


