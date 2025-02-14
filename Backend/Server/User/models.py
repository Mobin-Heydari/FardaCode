from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin




class User(AbstractUser, PermissionsMixin):
    """
    Custom User model that inherits from Django's AbstractUser  model.
    """
    # Email field with unique constraint and required
    email = models.EmailField(max_length=255, unique=True, blank=False)

    # Username field with unique constraint and required
    username = models.CharField(max_length=12, unique=True, blank=False)

    # Verified status field with default False
    is_verified = models.BooleanField(default=False)

    # Active status field with default True
    is_active = models.BooleanField(default=True)

    # Admin status field with default False
    is_admin = models.BooleanField(default=False)

    # Joined date field with auto_now_add
    joined_date = models.DateField(auto_now_add=True)

    # Set USERNAME_FIELD to email
    USERNAME_FIELD = "email"

    # Set REQUIRED_FIELDS to username and full_name
    REQUIRED_FIELDS = ["username", "full_name"]

    class Meta:
        """
        Meta class for User model.
        """
        # Set verbose name to User
        verbose_name = "User "

        # Set verbose name plural to Users
        verbose_name_plural = "Users"

        # Set ordering to joined_date
        ordering = ['joined_date']

    def __str__(self):
        """
        Returns a string representation of the User object.
        """
        return self.username

    def has_perm(self, perm, obj=None):
        """
        Returns True if the user has the specified permission.
        """
        return self.is_admin

    def has_module_perms(self, app_label):
        """
        Returns True if the user has permission to view the app.
        """
        return self.is_admin

    @property
    def is_staff(self):
        """
        Returns True if the user is a staff member.
        """
        # Simplest possible answer: All admins are staff
        return self.is_admin