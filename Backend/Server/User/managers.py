from django.db.models import Manager
from django.contrib.auth.models import BaseUserManager



class UserManager(BaseUserManager):
    # Method to create user with provided credentials
    def create_user(self, username, email, password=None, password_conf=None):
        """
        Creates a new user with the provided credentials.

        Args:
            username (str): The username for the new user.
            email (str): The email address for the new user.
            password (str, optional): The password for the new user. Defaults to None.
            password_conf (str, optional): The password confirmation for the new user. Defaults to None.

        Returns:
            User: The newly created user.
        """
        # Check if password and password_conf match
        if password and password_conf and password != password_conf:
            raise ValueError("Password and password confirmation do not match")

        email = email.lower()

        user = self.model(
            username=username,
            email=email,
        )

        # Set password for the user
        user.set_password(password)

        try:
            # Save the user to the database
            user.save(using=self._db)
        except Exception as e:
            # Handle any exceptions that occur during user creation
            raise ValueError("Failed to create user: {}".format(str(e)))

        return user

    # Method to create superuser with provided credentials
    def create_superuser(self, username, email, password=None):
        """
        Creates a new superuser with the provided credentials.

        Args:
            username (str): The username for the new superuser.
            email (str): The email address for the new superuser.
            password (str, optional): The password for the new superuser. Defaults to None.

        Returns:
            User: The newly created superuser.
        """
        # Normalize the email address
        normalized_email = self.normalize_email(email)

        # Check if password is not empty
        if not password:
            raise ValueError("Password cannot be empty")

        user = self.create_user(
            email=normalized_email,
            username=username,
            password=password,
        )

        # Set superuser flags
        user.is_admin = True
        user.is_superuser = True

        try:
            # Save the superuser to the database
            user.save(using=self._db)
        except Exception as e:
            # Handle any exceptions that occur during superuser creation
            raise ValueError("Failed to create superuser: {}".format(str(e)))

        return user