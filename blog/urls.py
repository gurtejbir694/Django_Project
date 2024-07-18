"""
URL configuration for clothes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views
urlpatterns = [
    path('', views.home, name='/'),
    path('contact/', views.contact, name="contact"),
    path('signin/', views.signin, name="signin"),
    path('login/', views.login, name="login"),
    path('categories/', views.books, name="categories"),
    path('products/<str:name>', views.library, name="products"),
    path('details/<str:cname>/<str:pname>', views.details, name="details"),
    path('authors/', views.authors, name='authors'),
    path('adetails/<str:aname>', views.about_author, name='adetails'),
    path('search/', views.search, name='search'),
    path('read/', views.read, name='read'),
    path('logout/', views.logout, name='logout'),
    path('freeread/', views.freeread, name='file')
    
]
