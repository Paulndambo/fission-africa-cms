from django.urls import path
from . views import *
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	#blog articles
	path("articles/", ArticleListView.as_view(), name="articles"),
	path("create-article/", CreateArticleView.as_view(), name="create-article"),
	path("article/<int:pk>/details/", ArticleDetailView.as_view(), name="article-details"),
	path("article/<int:pk>/update/", ArticleUpdateView.as_view(), name="update-article"),
	path("article/<int:pk>/delete/", ArticleDeleteView.as_view(), name="delete-article"),
	#press releases
	path("press-releases/", PressReleaseListView.as_view(), name="press-releases"),
	path("create-press-release/", CreatePressReleaseView.as_view(), name="create-press-release"),
	path("press-release/<int:pk>/details/", PressReleaseDetailView.as_view(), name="press-release-details"),
	path("press-release/<int:pk>/update/", PressReleaseUpdateView.as_view(), name="update-press-release"),
	path("press-release/<int:pk>/delete/", PressReleaseDeleteView.as_view(), name="delete-press-release"),

]