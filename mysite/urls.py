"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import article.views
import user.views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',article.views.index,name='index'),
    path('about/',article.views.about,name='about'),
    path('articles/',article.views.articles,name='articles'),
    path('article/<id>',article.views.article,name='detail'),
    path('allArticles/',article.views.allArticles,name='allArticles'),
    path('register/',user.views.register,name='register'),
    path('login/',user.views.loginUser,name='login'),
    path('comment/<id>',article.views.comment,name='comment'),
]
urlpatterns += staticfiles_urlpatterns()
