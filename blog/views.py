from django.shortcuts import render
from .models import Blog, Likes, Comments
from rest_framework.viewsets import ModelViewSet
from .serializers import BlogSerializer, LikeSerializer, CommentsSerializer
from rest_framework.authentication import BaseAuthentication, SessionAuthentication, TokenAuthentication
from .permissions import ClientPermission

class  BlogAPIView(ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    permission_classes=[ClientPermission]
    authentication_classes=[BaseAuthentication, SessionAuthentication]
  
  
class  LikeAPIView(ModelViewSet):
    queryset=Likes.objects.all()
    serializer_class=LikeSerializer
    permission_classes=[ClientPermission]
    authentication_classes=[BaseAuthentication, SessionAuthentication]
    
    
class  CommentAPIView(ModelViewSet):
    queryset=Comments.objects.all()
    serializer_class=CommentsSerializer
    permission_classes=[ClientPermission]
    authentication_classes=[BaseAuthentication, SessionAuthentication]  