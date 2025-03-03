from rest_framework import serializers
from .models import Category, Course, CourseSeason, Session, CourseContent, FaqCourse


class CategorySerializer(serializers.ModelSerializer):
    total_courses = serializers.IntegerField(source='courses.count', read_only=True)  # Adding total number of courses

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image', 'total_courses']


class SessionSerializer(serializers.ModelSerializer):

    duration_minutes = serializers.SerializerMethodField()  # Custom field for duration in minutes
    class Meta:
        model = Session
        fields = [
            'id', 'title', 'description', 'video', 'duration', 'duration_minutes', 
            'materials', 'order'
        ]

    def get_duration_minutes(self, obj):
        return int(obj.duration.total_seconds() // 60)  # Convert duration to minutes


class CourseSeasonSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True, read_only=True)  # Nested sessions
    total_sessions = serializers.IntegerField(source='sessions.count', read_only=True)  # Adding total number of sessions
    duration_hours = serializers.SerializerMethodField()  # Custom field for duration in hours

    class Meta:
        model = CourseSeason
        fields = [
            'id', 'title', 'summary', 'duration', 'duration_hours', 'order', 
            'total_sessions', 'sessions'
        ]

    def get_duration_hours(self, obj):
        return round(obj.duration.total_seconds() / 3600, 2)  # Convert duration to hours


class CourseContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseContent
        fields = [
            'id', 'title', 'content', 'image', 'video', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class FaqCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqCourse
        fields = [
            'id', 'question', 'answer', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class CourseSerializer(serializers.ModelSerializer):
    contents = CourseContentSerializer(many=True)
    faqs = FaqCourseSerializer(many=True)
    total_students = serializers.IntegerField(source='students.count', read_only=True)
    price_display = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'slug', 'description', 'category', 'status',
            'pricing_status', 'price', 'price_display', 'total_students',
            'poster', 'banner', 'introduction', 'duration', 
            'created_at', 'updated_at', 'contents', 'faqs'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'teacher': {'read_only': True},
            'students': {'read_only': True},
        }

    def get_price_display(self, obj):
        return f"${obj.price / 100:.2f}"


