from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views



app_name = "Authentication"


urlpatterns = [
    # Token Refresh View
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    # Login
    path('login/', views.LoginAPIView.as_view(), name="login"),
]