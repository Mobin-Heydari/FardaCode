from rest_framework.views import APIView, Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError

from User.models import User

from .serializers import LoginSerializer




# Define a class-based view for handling user login
class LoginAPIView(APIView):
    """
    Login view to authenticate users and return a JWT token.
    """
    
    # Define the POST method to handle login requests
    def post(self, request):
        """
        Handle POST requests to the login view.
        
        :param request: The incoming request object
        :return: A response object with the refresh and access tokens
        """
        
        # Create a serializer instance with the request data
        serializer = LoginSerializer(data=request.data)

        if request.user.is_authenticated:
            return Response({"message": "You are already authenticated"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Check if the serializer is valid
            if serializer.is_valid():
                # Extract the email from the validated data
                email = serializer.validated_data['email']
                
                # Retrieve the user instance from the database
                user = User.objects.get(email=email)

                # Check if the user is active
                if not user.is_active:
                    # Return an error response if the user is not active
                    return Response({'error': 'User  is not active'}, status=status.HTTP_401_UNAUTHORIZED)
                
                # Create a refresh token for the user
                refresh = RefreshToken.for_user(user)
                
                # Return a response with the refresh and access tokens
                return Response(
                    {
                        'refresh': str(refresh), 
                        'access': str(refresh.access_token)
                    },
                    status=status.HTTP_200_OK
                )
            else:
                # Return an error response with serializer errors
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Define a method to handle exceptions raised during view execution
    def handle_exception(self, exc):
        """
        Handle exceptions raised during view execution.
        
        :param exc: The exception object
        :return: A response object with an error message
        """
        
        # Check if the exception is a validation error
        if isinstance(exc, ValidationError):
            # Return a response with a validation error message
            return Response({'error': 'Validation error'}, status=status.HTTP_400_BAD_REQUEST)
        # Call the parent class's handle_exception method for other exceptions
        return super().handle_exception(exc)
