# Import necessary modules
from django.db import models





# Define the Profile model
class Profile(models.Model):
    """
    This model represents a user's profile.
    """
    # One-to-one relationship with the User model
    user = models.OneToOneField(
        'User.User',
        on_delete=models.CASCADE,
        related_name='Profile',
    )

    # Image field to store the user's profile picture
    image = models.ImageField(
        upload_to="Profiles/",  # Upload images to the 'Profiles' directory
        blank=True,  # Allow the image field to be blank
        null=True,  # Allow the image field to be null
    )

    # Age field to store the user's age
    age = models.PositiveIntegerField(null=True, blank=True)

    # Bio field to store the user's bio
    bio = models.TextField(blank=True)

    # LinkedIn field to store the user's LinkedIn profile URL
    linkedin_profile = models.URLField(null=True, blank=True)

    # GitHub field to store the user's GitHub profile URL
    github_profile = models.URLField(null=True, blank=True)

    # GitLab field to store the user's GitLab profile URL
    gitlab_profile = models.URLField(null=True, blank=True)

    # Instagram field to store the user's Instagram profile URL
    instagram_profile = models.URLField(null=True, blank=True)

    # YouTube field to store the user's YouTube profile URL
    youtube_profile = models.URLField(null=True, blank=True)

    # X field to store the user's X profile URL
    x_profile = models.URLField(null=True, blank=True)


    # Return the user's username as a string representation of the profile
    def __str__(self):
        return f'{self.user.username}'

    # Define the meta options for the Profile model
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"