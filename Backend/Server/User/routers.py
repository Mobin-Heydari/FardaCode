# Import the necessary modules
from rest_framework import routers
from django.urls import path, include

from .views import UserViewSet


# Define a custom router class
class UserRouter(routers.DefaultRouter):
    # Initialize the custom router
    def __init__(self):
        super().__init__()
        # Register the UserViewSet with the custom router
        self.register(r'', UserViewSet, basename='users')

    # Define a method to get the URLs for the custom router
    def get_urls(self):
        # Get the URLs from the parent class
        urls = super().get_urls()
        # Define custom URLs for the UserViewSet
        custom_urls = [
            # Define a URL pattern for the list view
            path('', include([
                # Define a URL pattern for the list view
                path('', UserViewSet.as_view({'get': 'list'})),
                # Define a URL pattern for the detail view
                path('<str:username>/', include([
                    # Define a URL pattern for the detail view
                    path('', UserViewSet.as_view({'get': 'retrieve'})),
                ])),
            ])),
        ]
        # Return the custom URLs
        return urls + custom_urls