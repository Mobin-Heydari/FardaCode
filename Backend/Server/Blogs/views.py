from django.shortcuts import get_object_or_404

from rest_framework.views import APIView, Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework import status

from . import serializers, models
from .permissions import IsSafeMethodOrStaff



class BlogViewSet(ModelViewSet):
    permission_classes = [IsSafeMethodOrStaff]
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    lookup_field = 'slug'


    def list(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, slug, *args, **kwargs):
        instance = get_object_or_404(models.Blog, slug=slug)
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({'Message': 'Blog created sucsesfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, slug, *args, **kwargs):
        instance = get_object_or_404(models.Blog, slug=slug)
        serializer = self.get_serializer(data=request.data, instance=instance, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsSafeMethodOrStaff]
    queryset = models.BlogCategory.objects.all()
    serializer_class = serializers.BlogCategorySerializer
    lookup_field = 'slug'


    def list(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, slug, *args, **kwargs):
        instance = get_object_or_404(models.BlogCategory, slug=slug)
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({'Message': 'Category created sucsesfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, slug, *args, **kwargs):
        instance = get_object_or_404(models.BlogCategory, slug=slug)
        serializer = self.get_serializer(data=request.data, instance=instance, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogContentViewSet(ViewSet):
    permission_classes = [IsSafeMethodOrStaff]

    def list(self, request, slug, *args, **kwargs):
        queryset = models.BlogContent.objects.filter(blog__slug=slug)
        serializer = serializers.BlogContentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, slug, content_id, *args, **kwargs):
        instance = get_object_or_404(models.BlogContent, blog__slug=slug, id=content_id)
        serializer = serializers.BlogContentSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, slug, *args, **kwargs):
        instance = get_object_or_404(models.Blog, slug=slug)
        serializer = serializers.BlogContentSerializer(data=request.data, context={'blog': instance})
        if serializer.is_valid():
            serializer.save()
            return Response({'Message': 'Content created sucsesfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, content_id, *args, **kwargs):
        instance = get_object_or_404(models.BlogContent, id=content_id)
        serializer = serializers.BlogContentSerializer(data=request.data, instance=instance, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)