from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status,generics
from .models import Post, Views_Post, Comment_Post
from .serializers import PostSerializer, CommentsPostSerializer
import random
from rest_framework import filters


class PostList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    search_fields = ['title','body','creator']
    filter_backends = (filters.SearchFilter,)
    queryset = Post.objects.all().filter(available=True)
    serializer_class =PostSerializer




class PostListRecommended(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    try:
        items = list(Post.objects.all())
        queryset = random.sample(items, 2)
        serializer_class = PostSerializer
    except:
        queryset = Post.objects.all()
        serializer_class = PostSerializer


# class PostListRecommended(APIView):
#     permission_classes = [permissions.AllowAny]

#     def get(self, request):
#         items = list(Post.objects.all())
#         random_items = random.sample(items, 2)
#         p_serializer = PostSerializer(random_items, many=True)
#         return Response(p_serializer.data, status=status.HTTP_200_OK)


class PostDetail(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        p = Post.objects.filter(id=pk)
        p_serializer = PostSerializer(p, many=True)
        return Response(p_serializer.data)


class CommentList(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        p = Comment_Post.objects.filter(for_post=pk)
        c_serializer = CommentsPostSerializer(p, many=True)
        return Response(c_serializer.data, status=status.HTTP_200_OK)


class CommentPost(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        name = data['name']
        email = data['email']
        body = data['body']
        post = data['post_id']
        try:
            if data['key'] and data['key'] == 'this_is_a_secret_key':
                get_post = Post.objects.get(id=post)
                comment = Comment_Post.objects.create(
                    name=name, email=email, body=body, for_post=get_post)
                comment.save()
                c_id = Comment_Post.objects.filter(for_post=get_post)
                c_serializer = CommentsPostSerializer(c_id, many=True)
                return Response(c_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# class ViewAdd(APIView):    <---- This code is yet to be debugged
#     permission_classes = [permissions.AllowAny]

#     def post(self, request):

#         rec_ip = int(request.data['ip'])
#         rec_for_post = int(request.data['for_post'])
#         all_ip = Views_Post.objects.filter(ip=rec_ip, for_post=rec_for_post)
#         is_post_valid = Post.objects.get(id=rec_ip)
#         print('hello')
#         if is_post_valid:
#             if all_ip:
#                 print(rec_ip+' exixts for ' + rec_for_post)
#                 return Response(status=HTTP_406_NOT_ACCEPTABLE)
#             else:
#                 new = Views_Post.objects.create(
#                     ip=rec_ip, for_post=rec_for_post)
#                 new.save()
#                 return Response(status=status.HTTP_201_CREATED)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)
