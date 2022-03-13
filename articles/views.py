from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from matplotlib import image

import articles

from .models import *
from .forms import *

def create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ArticleForm(request.POST, request.FILES)
            if form.is_valid():
                article = form.save(commit=False)
                article.author = request.user
                article.save()
            return redirect('home')

        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})
    else:
        return redirect('home')

def articleview(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = Comment.objects.order_by('-pub_date').filter(article=article)
    form = CommentForm()
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            comment = form.save(commit=False)
            comment.author = request.user
            comment.article = Article.objects.get(id=article_pk)
            comment.save()
        else:
            return render(request, 'articles/articleview.html', {'article': article, 'form': form, 'comments': comments, 'error': 'Писать комментарии могут только авторизованые пользователи'})
    return render(request, 'articles/articleview.html', {'article': article, 'form': form, 'comments': comments})

def myarticles(request):
    articles = Article.objects.order_by('-pub_date').filter(author=request.user)
    return render(request, 'articles/myarticles.html', {'articles': articles})

def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.author:
        if request.method == 'POST':
            article.delete()
            return redirect('myarticles')
        else:
            return redirect('myarticles')
    return redirect('home')

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk, author=request.user)
    if request.user == article.author:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
            return redirect('myarticles')
        form = ArticleForm(instance=article)
        return render(request, 'articles/updatearticle.html', {'form': form, 'id': article.id})
    else:
        return redirect('home')

def deletecomment(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk, author=request.user)
    if request.user == comment.author:
        if request.method == 'POST':
            comment.delete()
    return redirect(reverse("articleview", args=(comment.article.id,)))
