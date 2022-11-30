from django.urls import path, include
from .models import Post, Views_Post, Comment_Post
from rest_framework import routers, serializers, viewsets


class PostSerializer(serializers.ModelSerializer):
    html = serializers.SerializerMethodField()
    plain = serializers.SerializerMethodField()

    def get_html(self, instance):
        return str(instance.body.html)

    def get_plain(self, instance):
        return str(instance.body.plain)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'date_added',
                  'creator', 'likes', 'views', 'poster','html','plain']


class ViewPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Views_Post
        fields = '__all__'


class CommentsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment_Post
        fields = ['body', 'commented_on', 'for_post', 'name', 'email']
