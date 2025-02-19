# Import the necessary modules
from django.urls import path, include
from . import routers
from . import views


app_name = "Courses"

course_router = routers.CourseRouter()

urlpatterns = [
    path('', include(course_router.get_urls()))
]
