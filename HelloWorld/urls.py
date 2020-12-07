"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

# from django.conf.urls import url

from django.urls import re_path, path

from . import views

from django.contrib import admin

urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path(r'^$', views.hello),
    # re_path(r'^hello$',views.hello),
    path('hello/', views.hello),
    path('add_book/', views.add_book),
    path('search_book/', views.search_book),
    path('delete_book/', views.delete_book),
    path('modify_book/', views.modify_book),
    path('add_books/', views.add_books),
    re_path(r'^admin/', admin.site.urls),
    path('caculate_book/', views.caculate_book),
    path('index/',views.index),
]
