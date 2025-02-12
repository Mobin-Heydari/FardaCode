from django.urls import path, include

from .routers import BlogsRouter


app_name = "Blogs"

blogs_router = BlogsRouter()

urlpatterns = [
    path('', include(blogs_router.get_urls()))
]
