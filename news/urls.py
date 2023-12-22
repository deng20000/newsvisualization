from django.urls import path, re_path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # This line defines the path for the home page
    path("", views.index, name="index"),
    # This line defines the path for the API endpoint for retrieving a list of users
    # re_path(r'^api/v1/users/$', views.UserList.as_view(), name='user-list')
    # This line defines the path for the API endpoint for retrieving a news article
    # re_path(r'^news/$', views.news_articles),
    # This line defines the path for the API endpoint for retrieving a news article detail
    # re_path(r'^news/(?P<pk>\d+)/$', views.news_article_detail),


]

urlpatterns = format_suffix_patterns(urlpatterns)



