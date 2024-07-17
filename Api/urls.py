from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("", views.ArticleList.as_view(),name="list"),
    path("<slug:slug>/", views.ArticleDetail.as_view(),name="detail"),
    path("<int:pk>/delete/", views.JustDeleteArticle.as_view(),name="delete"),

    path("users/", views.UserList.as_view(),name="users_list"),
    path("users/<int:pk>/", views.UserDetail.as_view(),name="users_detail"),
]