from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Profile
from .serializers import ProfileSerializer

from User.models import User



class ProfileViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Profile model.
    """
    # Define the queryset for the viewset
    queryset = Profile.objects.all()
    # Define the serializer class for the viewset
    serializer_class = ProfileSerializer
    # Define the permission classes for the viewset
    permission_classes = [IsAuthenticated]
    # Defines the required field for retrieve methods
    lookup_field = 'user_username'

    # Define the list method for the viewset
    def list(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve a list of profiles.
        """
        # Retrieve the queryset
        queryset = Profile.objects.all()
        # Serialize the queryset
        serializer = self.serializer_class(queryset, many=True)
        # Return the serialized data
        return Response(serializer.data)

    # Define the retrieve method for the viewset
    def retrieve(self, request, user_username, *args, **kwargs):
        """
        Handle GET requests to retrieve a single profile.
        """
        # Getting the user instance
        instance = get_object_or_404(User, username=user_username)
        # Retrieve the profile instance
        queryset = get_object_or_404(Profile, user=instance)
        # Serialize the profile instance
        serializer = self.serializer_class(queryset)
        # Return the serialized data
        return Response(serializer.data)
    

    # Define the update method for the viewset
    def update(self, request, user_username, *args, **kwargs):
        # Getting the user instance
        instance = get_object_or_404(User, username=user_username)
        # Retrieve the profile instance
        queryset = get_object_or_404(Profile, user=instance)
        # Serialize the profile instance
        serializer = self.serializer_class(queryset, data=request.data, partial=True)
        # Validate the serializer
        serializer.is_valid(raise_exception=True)
        # Update the profile instance
        serializer.save()
        # Return the serialized data
        return Response(serializer.data, status.HTTP_202_ACCEPTED)