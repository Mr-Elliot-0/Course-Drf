# from django.shortcuts import render
from .serializers import ArticleSerializer,UserSerializer
from Blog.models import Article,User
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView,CreateAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.

class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(status=True)
    serializer_class = ArticleSerializer

class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
