from django.urls import path, include

from .routers import BlogsRouter, CategoriesRouter


app_name = "Blogs"

blogs_router = BlogsRouter()
categories_router = CategoriesRouter()

urlpatterns = [
    path('', include(blogs_router.get_urls())),
    path('categories/', include(categories_router.get_urls()))
]
