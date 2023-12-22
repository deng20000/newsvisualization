"""newsvisualization URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from news.views import show_test,show_mongodb_test, NewsAPIView
# from news.views import get_api
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('get_api/', get_api),
    path('polls/', include("news.urls")),
    # path('api-auth/', include('rest_framework.urls'))
    path('v1/', include('news.urls')),
    path('test/', show_test),
    path("show/", show_mongodb_test),
    path('api/news/',NewsAPIView.as_view(),name = 'news-api')
]
