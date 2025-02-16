from django.test import TestCase
from User.models import User
from datetime import timedelta
from .models import Category, Course, CourseSeason, Session

class CourseTestCase(TestCase):

    def setUp(self):
        # Create a category
        self.category = Category.objects.create(
            name='Programming',
            slug='programming'
        )

        # Create a user
        self.teacher = User.objects.create_user(
            username='teacher1',
            password='password123',
            email='teacher1@gmail.com'
        )

        # Create a course
        self.course = Course.objects.create(
            teacher=self.teacher,
            title='Django Development',
            slug='django-development',
            category=self.category,
            description='Learn Django development from scratch.',
        )

        # Create a course season
        self.course_season = CourseSeason.objects.create(
            course=self.course,
            title='Introduction to Django',
            order=1
        )

        # Create a session
        self.session = Session.objects.create(
            season=self.course_season,
            title='Getting Started with Django',
            video='path/to/video.mp4',
            duration=timedelta(minutes=30),  # Use timedelta for duration
            order=1
        )

    def test_course_creation(self):
        self.assertEqual(self.course.title, 'Django Development')
        self.assertEqual(self.course.teacher.username, 'teacher1')
        self.assertEqual(self.course.category.name, 'Programming')
        self.assertEqual(self.course_season.course.title, 'Django Development')
        self.assertEqual(self.course_season.title, 'Introduction to Django')
        self.assertEqual(self.session.season.title, 'Introduction to Django')
        self.assertEqual(self.session.title, 'Getting Started with Django')
        self.assertEqual(self.session.duration, timedelta(minutes=30))  # Use timedelta for comparison

    def test_course_duration_update(self):
        self.course_season.refresh_from_db()
        self.assertEqual(self.course_season.duration, self.session.duration)

        self.course.refresh_from_db()
        self.assertEqual(self.course.duration, self.course_season.duration)
