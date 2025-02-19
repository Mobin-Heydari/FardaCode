from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response
from .models import Course, Category
from .serializers import CourseSerializer, CategorySerializer



class CourseViewSet(ViewSet):
    """
    A ViewSet for listing, retrieving, creating, updating, and deleting courses.
    """
    lookup_field = 'slug'

    def list(self, request):
        """
        List all courses.

        Retrieves all courses from the database and serializes them.
        """
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, slug):
        """
        Retrieve a course by (slug).

        If the course is found, it is serialized and returned.
        If not, a 404 Not Found response is returned.
        """
        queryset = Course.objects.all()
        course = get_object_or_404(queryset, slug=slug)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new course.

        Validates the incoming data and creates a new course if valid.
        Returns the serialized data of the created course with a 201 status.
        If validation fails, returns a 400 Bad Request response with errors.
        """
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, slug):
        """
        Update an existing course by (slug).

        Validates the incoming data and updates the course if valid.
        Returns the serialized data of the updated course.
        If validation fails, returns a 400 Bad Request response with errors.
        """
        course = get_object_or_404(Course, slug=slug)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, slug):
        """
        Delete a course by (slug).

        If the course is found, it is deleted and a 204 No Content response is returned.
        If not, a 404 Not Found response is returned.
        """
        course = get_object_or_404(Course, slug=slug)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CategoryViewSet(ViewSet):
    lookup_field = 'slug'

    def list(self, request):
        """
        List all categories.

        Retrieves all categories from the database and serializes them.
        """
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, slug=None):
        """
        Retrieve a category by its slug.

        If the category is found, it is serialized and returned.
        If not, a 404 Not Found response is returned.
        """
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, slug=slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new category.

        Validates the incoming data and creates a new category if valid.
        Returns the serialized data of the created category with a 201 status.
        If validation fails, returns a 400 Bad Request response with errors.
        """
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, slug=None):
        """
        Update an existing category by its slug.

        Validates the incoming data and updates the category if valid.
        Returns the serialized data of the updated category.
        If validation fails, returns a 400 Bad Request response with errors.
        """
        category = get_object_or_404(Category, slug=slug)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, slug=None):
        """
        Delete a category by its slug.

        If the category is found, it is deleted and a 204 No Content response is returned.
        If not, a 404 Not Found response is returned.
        """
        category = get_object_or_404(Category, slug=slug)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)