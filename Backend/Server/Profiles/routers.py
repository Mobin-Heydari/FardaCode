# Import the necessary modules
from rest_framework import routers
from django.urls import path, include

from .views import ProfileViewSet


# Define a custom router class for the ProfileViewSet
class ProfileRouter(routers.DefaultRouter):
    # Initialize the custom router
    def __init__(self):
        super().__init__()
        # Register the ProfileViewSet with the custom router
        self.register(r'', ProfileViewSet, basename='profiles')

    # Define a method to get the URLs for the custom router
    def get_urls(self):
        # Get the URLs from the parent class
        urls = super().get_urls()
        # Define custom URLs for the ProfileViewSet
        custom_urls = [
            # Define a URL pattern for the list view
            path('', include([
                # Define a URL pattern for the list view
                path('', ProfileViewSet.as_view({'get': 'list'})),
                # Define a URL pattern for the detail view
                path('<str:user_username>/', include([
                    # Define a URL pattern for the detail view
                    path('', ProfileViewSet.as_view({'get': 'retrieve'})),
                ])),
            ])),
        ]
        # Return the custom URLs
        return urls + custom_urls