from rest_framework import serializers

from .models import Blog, BlogCategory, BlogComment, BlogContent




class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = '__all__'


class BlogContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogContent
        fields = '__all__'

class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = '__all__'



class BlogSerializer(serializers.ModelSerializer):

    category = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'
    

    def get_category(self, obj):
        return obj.category.name
    
    def get_content(self, obj):
        queryset = BlogContent.objects.filter(blog=obj)
        serializer = BlogContentSerializer(queryset, many=True)
        return serializer.data