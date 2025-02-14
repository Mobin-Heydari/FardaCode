# Import the necessary modules
from django.urls import path, include
from .routers import UserRouter

app_name = "Users"

# Create an instance of the custom router
router = UserRouter()

# Define the URL patterns for the application
urlpatterns = [
    # Include the custom router URLs
    path('', include(UserRouter().urls)),
]