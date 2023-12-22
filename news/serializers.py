from django.contrib.auth import get_user_model
from .models import NewsArticle
from rest_framework import serializers

User = get_user_model()

class NewsArticleSerializer(serializers.Serializer):

    # source_id is a string with a maximum length of 100 and is optional
    source_id = serializers.CharField(max_length=100, allow_null=True)
    # source_name is a string with a maximum length of 100
    source_name = serializers.CharField(max_length=100)
    # author is a string with a maximum length of 100 and is optional
    author = serializers.CharField(max_length=100, allow_null=True)
    # title is a string with a maximum length of 200
    title = serializers.CharField(max_length=200)
    # description is a string
    description = serializers.CharField()
    # url is a URL field
    url = serializers.URLField()
    # url_to_image is a URL field and is optional
    url_to_image = serializers.URLField(allow_null=True)
    # published_at is a DateTime field
    published_at = serializers.DateTimeField()
    # content is a string
    content = serializers.CharField()

    # create method to create a NewsArticle object with the validated data
    def create(self, validated_data):
        return NewsArticle.objects.create(**validated_data)

    # update method to update an existing NewsArticle object with the validated data
    def update(self, instance, validated_data):
        instance.source_id = validated_data.get('source_id', instance.source_id)
        instance.source_name = validated_data.get('source_name', instance.source_name)
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.url = validated_data.get('url', instance.url)
        instance.url_to_image = validated_data.get('url_to_image', instance.url_to_image)
        instance.published_at = validated_data.get('published_at', instance.published_at)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance


