from rest_framework import serializers
from rest_framework import validators

from rest_framework_simplejwt.tokens import RefreshToken

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
    


class UserRegisterSerializer(serializers.Serializer):
    """
    Serializer to validate user registration data.
    """
    
    # Define the email field with validation to ensure uniqueness
    email = serializers.EmailField(
        validators=[
            validators.UniqueValidator(queryset=User.objects.all())  # Ensure email is unique in User model
        ],
        required=True,  # Email is required
        help_text="Enter a unique email address"  # Help text for the email field
    )

    # Define the username field
    username = serializers.CharField(
        validators=[
            validators.UniqueValidator(queryset=User.objects.all())  # Ensure username is unique in User model
        ],
        required=True,  # Username is required
        help_text="Enter a unique username"  # Help text for the username field
    )

    # Define the password field with validation
    password = serializers.CharField(
        required=True,  # Password is required
        write_only=True,  # Password is not returned in the response
        help_text="Enter a password (8-16 characters)"  # Help text for the password field
    )

    # Define the password confirmation field
    password_conf = serializers.CharField(
        required=True,  # Password confirmation is required
        write_only=True,  # Password confirmation is not returned in the response
        help_text="Confirm your password (8-16 characters)"  # Help text for the password confirmation field
    )


    # Validate the password field
    def validate_password(self, value):
        # Check if the password length is within the allowed range
        if len(value) < 8 or len(value) > 16:
            raise serializers.ValidationError('Password must be at least 8 characters long and the most 16 characters long')
        return value

    # Validate the password_conf field
    def validate_password_conf(self, value):
        # Check if the password_conf length is within the allowed range
        if len(value) < 8 or len(value) > 16:
            raise serializers.ValidationError('Password must be at least 8 characters long and the most 16 characters long')
        return value

    # Validate the username field
    def validate_username(self, value):
        # Check if the username length is within the allowed range
        if len(value) < 3 or len(value) > 20:
            raise serializers.ValidationError('Username must be between 3 and 20 characters long')
        return value


    # Validate the entire serializer
    def validate(self, attrs):
        # Check if the password and password_conf match
        if attrs['password'] != attrs['password_conf']:
            raise serializers.ValidationError('Passwords do not match')
        if attrs['password'] == attrs['username']:
            raise serializers.ValidationError('Password cannot be the same as the username')
        if len(attrs['password']) < 8 or len(attrs['password']) > 16:
            raise serializers.ValidationError('Password must be between 8 and 16 characters long')
        return attrs

    # Create a new user instance
    def create(self, validated_data):
        # Create a new user instance
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
        )

        # Save the user to the database
        user.save()

        # Generate tokens for the user
        refresh = RefreshToken.for_user(user)

        # Return user data and tokens
        return {
            'user': {
                'username': user.username,
                'email': user.email,
                # Add any other user fields you want to return
            },
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }