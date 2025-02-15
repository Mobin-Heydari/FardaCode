# Import necessary modules
from rest_framework import serializers
from .models import Profile




class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.
    """

    user = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = "__all__"
        exelude = ["id"]
        

    def get_user(slef, obj):
        return str(obj.user.username)
    

    def update(self, instance, validated_data):
        """
        Update the profile instance with the validated data.
        """
        instance.image = validated_data.get('image', instance.image)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.linkedin_profile = validated_data.get('linkedin_profile', instance.linkedin_profile)
        instance.github_profile = validated_data.get('github_profile', instance.github_profile)
        instance.gitlab_profile = validated_data.get('gitlab_profile', instance.gitlab_profile)
        instance.instagram_profile = validated_data.get('instagram_profile', instance.instagram_profile)
        instance.youtube_profile = validated_data.get('youtube_profile', instance.youtube_profile)
        instance.x_profile = validated_data.get('x_profile', instance.x_profile)
        instance.save()
        return instance