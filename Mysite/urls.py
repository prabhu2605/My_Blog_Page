"""
URL configuration for Mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import (welcome, login, snapchat, instagram, about, registration,
                        blog, Create_blog, blog_details, EditBlog, Changeblog, blogupdated, blogdelete)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='welcome'),
    path('login/', login, name='login'),
    path('about/', about, name='about'),
    path('insta/', instagram, name='insta'),
    path('snap/', snapchat, name='snap'),
    path('register/', registration, name='register'),
    path('blog/', blog, name='blog'),
    path('create_blog/', Create_blog, name='create'),
    path('blog_details/', blog_details, name='details'),
    path('edit_blog/', EditBlog, name='edit'),
    path('change_blog/', Changeblog, name='change'),
    path('updated_blog/', blogupdated, name='updated'),
    path('delete_blog/', blogdelete, name='delete')
]

