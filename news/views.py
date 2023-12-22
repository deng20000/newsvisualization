from django.shortcuts import render
import json
import requests
# Create your views here.
import requests

# from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import NewsArticleSerializer
from .models import NewsArticle
from rest_framework.response import Response

# 使用基于APIView的视图
from rest_framework.views import APIView
from django.http import Http404
from .models import NewsArticle, News

import json

class NewsArticles(APIView):
    def get(self, request):
        articles = NewsArticle.objects.all()
        serializer = NewsArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NewsArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NewsArticleDetail(APIView):
    def get_object(self, pk):
        try:
            return NewsArticle.objects.get(pk=pk)
        except NewsArticle.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = NewsArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = NewsArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#
def get_api(request):
    # Set the URL for the API call
    url = "https://newsapi.org/v2/everything?q=科技&from=2023-10-27&to=2023-10-29&sortBy=popularity&language=zh&apiKey=b4f080f0c1834adfa203e577d141be21"
    # Make the API call and store the response
    response = requests.get(url)
    print(response.status_code)
    print(response.json())

    return render(request, 'test.html', {'response': response})

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def show_test(request):
    with open("scraper/scraper/spiders/test.json") as f:
        data = json.load(f)
    context = {
        'data': data
    }
    return render(request, "test.html", context)

def show_mongodb_test(request):
    news = News.objects.all()
    return render(request, "news_vue2.html", {"news": news})


# @api_view(['GET', 'POST'])
# def news_articles(request):
#     '''
#     GET:
#     Returns a list of all news articles
#     POST:
#     Creates a new news article
#     '''
#     if request.method == 'GET':
#         # Get all news articles from the database
#         articles = NewsArticle.objects.all()
#         # Serialize the articles into a JSON format
#         serializer = NewsArticleSerializer(articles, many=True)
#         # Return the serialized data
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         # Deserialize the data into a model format
#         serializer = NewsArticleSerializer(data=request.data)
#         # Check if the data is valid
#         if serializer.is_valid():
#             # Save the data to the database
#             serializer.save()
#             # Return the serialized data with a status code of 201 CREATED
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # Return the errors with a status code of 400 BAD REQUEST
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def news_article_detail(request, pk):
#     '''
#     Retrieve, update or delete a news article.
#     '''
#     try:
#         article = NewsArticle.objects.get(pk=pk)
#     except NewsArticle.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = NewsArticleSerializer(article)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = NewsArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class NewsAPIView(APIView):
    def get(self, request, format=None):
        news_articles = NewsArticle.objects.all()
        serializer = NewsArticleSerializer(news_articles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NewsArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
