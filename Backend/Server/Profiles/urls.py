# Import the necessary modules
from django.urls import path, include

# Import the custom routers
from .routers import ProfileRouter

app_name = "Profiles"

# Create instances of the custom routers
profile_router = ProfileRouter()
# Define the URL patterns
urlpatterns = [
    path('', include(profile_router.get_urls()))
]