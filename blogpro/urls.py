from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls), 
    path("auth/",include("userservice.urls")),  # the urls for the authentication system
    path("api/",include("blogservice.urls")), # the urls for the blog system
]
