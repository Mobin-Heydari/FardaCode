from rest_framework import serializers
from .models import Category, Course, CourseSeason, Session, Faq, Content



class SessionSerializer(serializers.ModelSerializer):
    season_title = serializers.CharField(source='season.title', read_only=True)  # Adding related season title
    course_title = serializers.CharField(source='season.course.title', read_only=True)  # Adding related course title
    duration_minutes = serializers.SerializerMethodField()  # Custom field for duration in minutes

    class Meta:
        model = Session
        fields = [
            'id', 'title', 'description', 'video', 'duration', 'duration_minutes', 
            'materials', 'quizzes', 'objectives', 'prerequisites', 'order', 
            'season_title', 'course_title', 'created_at', 'updated_at'
        ]

    def get_duration_minutes(self, obj):
        return int(obj.duration.total_seconds() // 60)  # Convert duration to minutes

class CourseSeasonSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True, read_only=True)  # Nested sessions
    total_sessions = serializers.IntegerField(source='sessions.count', read_only=True)  # Adding total number of sessions
    course_title = serializers.CharField(source='course.title', read_only=True)  # Adding related course title
    duration_hours = serializers.SerializerMethodField()  # Custom field for duration in hours

    class Meta:
        model = CourseSeason
        fields = [
            'id', 'title', 'summary', 'duration', 'duration_hours', 'objectives', 
            'resources', 'prerequisites', 'start_date', 'end_date', 'order', 
            'total_sessions', 'course_title', 'sessions', 'created_at', 'updated_at'
        ]

    def get_duration_hours(self, obj):
        return round(obj.duration.total_seconds() / 3600, 2)  # Convert duration to hours

class CourseSerializer(serializers.ModelSerializer):
    seasons = CourseSeasonSerializer(many=True, read_only=True)  # Nested seasons
    total_seasons = serializers.IntegerField(source='seasons.count', read_only=True)  # Adding total number of seasons
    teacher_name = serializers.CharField(source='teacher.get_full_name', read_only=True)  # Adding teacher's full name
    average_rating = serializers.DecimalField(max_digits=3, decimal_places=2, read_only=True)  # Adding average rating
    total_students = serializers.IntegerField(source='students.count', read_only=True)  # Adding total number of students
    price_display = serializers.SerializerMethodField()  # Custom field for formatted price

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'slug', 'description', 'category', 'status', 'pricing_status', 
            'price', 'price_display', 'teacher_name', 'total_seasons', 'total_students', 
            'average_rating', 'poster', 'banner', 'introduction', 'duration', 
            'level', 'language', 'prerequisites', 'certification', 'objectives', 'syllabus', 
            'tags', 'created_at', 'updated_at', 'seasons'
        ]

    def get_price_display(self, obj):
        return f"${obj.price / 100:.2f}"  # Format price as currency

class CategorySerializer(serializers.ModelSerializer):
    total_courses = serializers.IntegerField(source='courses.count', read_only=True)  # Adding total number of courses

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image', 'total_courses']

class FaqSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)  # Adding related course title

    class Meta:
        model = Faq
        fields = ['id', 'question', 'answer', 'course', 'course_title']

class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = ['id', 'title', 'text_content', 'image', 'video', 'course', 'created_at', 'updated_at']
