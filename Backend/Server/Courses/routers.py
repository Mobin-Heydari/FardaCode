# Import the necessary modules
from rest_framework import routers
from django.urls import path, include

from .views import CourseViewSet, CategoryViewSet


# Define a custom router class for the CourseViewSet
class CourseRouter(routers.DefaultRouter):
    # Initialize the custom router
    def __init__(self):
        super().__init__()
        # Register the CourseViewSet with the custom router
        self.register(r'', CourseViewSet, basename='Courses')

    # Define a method to get the URLs for the custom router
    def get_urls(self):
        # Define custom URLs for the CourseViewSet
        custom_urls = [
            # Define a URL pattern for the list view
            path('', include([
                # Define a URL pattern for the list view
                path('', CourseViewSet.as_view({'get': 'list'})),
                # Create view
                path('', CourseViewSet.as_view({'post': 'create'})),
                # Detail view
                path('detail/<slug:slug>/', CourseViewSet.as_view({'get': 'retrieve'})),
                # Update view
                path('update/<slug:slug>/', CourseViewSet.as_view({'put': 'update'})),
                # Delete view
                path('delete/<slug:slug>/', CourseViewSet.as_view({'delete': 'detroy'})),
            ])),
        ]
        # Return the custom URLs
        return custom_urls
    


# Define a custom router class for the CategoryViewSet
class CategoryRouter(routers.DefaultRouter):
    # Initialize the custom router
    def __init__(self):
        super().__init__()
        # Register the CategoryViewSet with the custom router
        self.register(r'categories/', CategoryViewSet, basename='Categories')

    # Define a method to get the URLs for the custom router
    def get_urls(self):
        # Define custom URLs for the CategoryViewSet
        custom_urls = [
            # Define a URL pattern for the list view
            path('', include([
                # Define a URL pattern for the list view
                path('', CategoryViewSet.as_view({'get': 'list'})),
                # Create view
                path('', CategoryViewSet.as_view({'post': 'create'})),
                # Detail view
                path('detail/<slug:slug>', CategoryViewSet.as_view({'get': 'retrieve'})),
                # Update view
                path('update/<slug:slug>/', CategoryViewSet.as_view({'put': 'update'})),
                # Delete view
                path('delete/<slug:slug>/', CategoryViewSet.as_view({'delete': 'detroy'})),
            ])),
        ]
        # Return the custom URLs
        return custom_urls