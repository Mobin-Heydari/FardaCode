from django.urls import path, include

from .routers import BlogsRouter, CategoriesRouter, BlogContentsRouter


app_name = "Blogs"

blogs_router = BlogsRouter()
categories_router = CategoriesRouter()
blog_contents_router = BlogContentsRouter()

urlpatterns = [
    path('', include(blogs_router.get_urls())),
    path('categories/', include(categories_router.get_urls())),
    path('content/', include(blog_contents_router.get_urls())),
]
