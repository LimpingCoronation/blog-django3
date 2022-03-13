from django.forms import ModelForm

from .models import *

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['image', 'title', 'text']
        labels = {
            'image': ('Изображение'),
            'title': ('Заголовок'),
            'text': ('Текст'),
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': ('Текст'),
        }

