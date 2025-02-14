from rest_framework import serializers
from User.models import User




# Define the LoginSerializer class
class LoginSerializer(serializers.Serializer):
    """
    Serializer to validate email and password.
    """
    # Define the email field
    email = serializers.CharField(max_length=255)
    
    # Define the password field
    password = serializers.CharField(max_length=255, write_only=True)

    # Validate the email field
    def validate_email(self, value):
        # Check if the email exists in the database
        if not User.objects.filter(email=value).exists():
            # Raise a validation error if the email does not exist
            raise serializers.ValidationError('email does not exist')
        # Return the validated email
        return value

    # Validate the password field
    def validate_password(self, value):
        # Check if the password is at least 8 characters long
        if len(value) < 8:
            # Raise a validation error if the password is too short
            raise serializers.ValidationError('Password must be at least 8 characters long')
        # Return the validated password
        return value

    # Validate the entire serializer
    def validate(self, data):
        # Get the email and password from the data
        email = data.get('email')
        password = data.get('password')
        
        # Check if both email and password are provided
        if email is None or password is None:
            # Raise a validation error if either email or password is missing
            raise serializers.ValidationError('Both email and password are required')
        
        # Get the user object from the database
        user = User.objects.get(email=email)
        
        # Check if the password is correct
        if not user.check_password(password):
            # Raise a validation error if the password is incorrect
            raise serializers.ValidationError('Invalid password')
        
        # Return the validated data
        return data