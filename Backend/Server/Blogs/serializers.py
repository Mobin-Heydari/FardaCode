from rest_framework import serializers
from .models import BlogCategory, Blog, BlogContent, BlogComment


class BlogCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogCategory
        fields = '__all__'


    def create(self, validated_data):
        queryset = BlogCategory.objects.create(**validated_data)
        queryset.save()

        return queryset
    

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        
        return instance


class BlogContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogContent
        fields = '__all__'


class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(read_only=True)
    blog_content = BlogContentSerializer(many=True, read_only=True)
    category_id = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = Blog
        fields = '__all__'

    def create(self, validated_data):
        category_id = validated_data.pop('category_id')
        category = BlogCategory.objects.get(id=category_id)
        
        blog = Blog.objects.create(category=category, **validated_data)

        return blog

    def update(self, instance, validated_data):
        category_id = validated_data.pop('category_id', None)

        if category_id is not None:
            category = BlogCategory.objects.get(id=category_id)
            instance.category = category

        instance.title = validated_data.get('title', instance.title)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.content = validated_data.get('content', instance.content)
        instance.status = validated_data.get('status', instance.status)
        instance.image = validated_data.get('image', instance.image)
        instance.views = validated_data.get('views', instance.views)
        instance.likes = validated_data.get('likes', instance.likes)
        instance.dislikes = validated_data.get('dislikes', instance.dislikes)
        instance.save()

        return instance
