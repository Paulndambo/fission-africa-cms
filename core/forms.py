from django import forms
from . models import Article, PressRelease

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'username', 'type': 'hidden'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            #'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            #'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'username', 'type': 'hidden'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            #'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            #'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


class PressReleaseForm(forms.ModelForm):
    class Meta:
        model = PressRelease
        fields = ('title', 'body', 'created_by')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'username', 'type': 'hidden'}),
            'created_by': forms.Select(attrs={'class': 'form-control'}),
            #'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            #'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditPressReleaseForm(forms.ModelForm):
    class Meta:
        model = PressRelease
        fields = ('title', 'body', 'created_by')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'username', 'type': 'hidden'}),
            'created_by': forms.Select(attrs={'class': 'form-control'}),
            #'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            #'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }