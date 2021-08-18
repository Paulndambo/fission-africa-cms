from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.
class Article(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=500)
	#body = models.TextField(blank=True)
	body = RichTextField(blank=True, null=True)
	date_posted = models.DateField(default=timezone.now)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("articles")

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
	name = models.CharField(max_length=200)
	comment = models.CharField(max_length=500)
	date_posted = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.name + " Commented on "+str(self.article)

class PressRelease(models.Model):
	created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=200)
	body = RichTextField(blank=True, null=True)
	date_released = models.DateField(default=timezone.now)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("press-releases")

    