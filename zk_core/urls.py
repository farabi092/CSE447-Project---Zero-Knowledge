"""
URL configuration for zk_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from network.views import AdminConsoleView, AdminUserPostsPageView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')), 
    path('api/network/', include('network.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('feed/', TemplateView.as_view(template_name='feed.html'), name='feed'),
    path('admin-console/', AdminConsoleView.as_view(), name='admin_console'),
    path('admin-console/users/<int:user_id>/posts/', AdminUserPostsPageView.as_view(), name='admin_user_posts_page'),
]
