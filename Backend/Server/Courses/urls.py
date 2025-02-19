# Import the necessary modules
from django.urls import path, include
from . import routers

app_name = "Courses"

course_router = routers.CourseRouter()
category_router = routers.CategoryRouter()

urlpatterns = [
    path('', include(course_router.get_urls())),
    path('categories/', include(category_router.get_urls()))
]
