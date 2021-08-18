from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView, DetailView, DeleteView, UpdateView
from . models import Article, PressRelease
from django.contrib.auth.models import User
from . forms import ArticleForm, EditArticleForm, PressReleaseForm, EditPressReleaseForm
from django.urls import reverse_lazy
# Create your views here.
def home(request):
	users = User.objects.all().count()
	articles = Article.objects.all().count()
	press_releases = PressRelease.objects.all()

	context = {
		"users": users,
		"articles": articles,
		"press_releases": press_releases
	}

	return render(request, "index.html", context)


class PressReleaseListView(ListView):
	model = PressRelease
	template_name = "press-release.html"

class CreatePressReleaseView(CreateView):
	model = Article
	#fields = "__all__"
	form_class = PressReleaseForm
	template_name = "new-press-release.html"

class PressReleaseDetailView(DetailView):
	model = PressRelease
	template_name = "view-press-release.html"

class PressReleaseUpdateView(UpdateView):
	model = PressRelease
	#fields = ["author", "title", "body"]
	form_class = EditPressReleaseForm
	template_name = "update-press-release.html"

class PressReleaseDeleteView(DeleteView):
	model = PressRelease
	template_name = "delete-press-release.html"
	success_url = reverse_lazy("articles")


class ArticleListView(ListView):
	model = Article
	template_name = "articles.html"

class CreateArticleView(CreateView):
	model = Article
	#fields = "__all__"
	form_class = ArticleForm
	template_name = "add-article.html"

class ArticleDetailView(DetailView):
	model = Article
	template_name = "view-article.html"

class ArticleUpdateView(UpdateView):
	model = Article
	#fields = ["author", "title", "body"]
	form_class = EditArticleForm
	template_name = "update-article.html"

class ArticleDeleteView(DeleteView):
	model = Article
	template_name = "delete-article.html"
	success_url = reverse_lazy("articles")