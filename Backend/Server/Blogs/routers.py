from django.urls import path, include

from rest_framework import routers

from . import views




class BlogsRouter(routers.DefaultRouter):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.register(r'', views.BlogViewSet, basename='blogs')

    

    def get_urls(self):
        custom_urls = [
            path('', include([
                path('', views.BlogViewSet.as_view({'get': 'list'})),
                path('create/', views.BlogViewSet.as_view({'post': 'create'})),
                path('<slug:slug>/', views.BlogViewSet.as_view({'get': 'retrieve'})),
                path('update/<slug:slug>/', views.BlogViewSet.as_view({'put': 'update'})),
            ]))
        ]

        return custom_urls
    
class CategoriesRouter(routers.DefaultRouter):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.register(r'categories/', views.BlogViewSet, basename='categories')

    

    def get_urls(self):
        custom_urls = [
            path('', include([
                path('', views.CategoryViewSet.as_view({'get': 'list'})),
                path('create/', views.CategoryViewSet.as_view({'post': 'create'})),
                path('<slug:slug>/', views.CategoryViewSet.as_view({'get': 'retrieve'})),
                path('update/<slug:slug>/', views.CategoryViewSet.as_view({'put': 'update'})),
            ]))
        ]

        return custom_urls