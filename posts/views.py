from django.shortcuts import render

from posts.models import Article

# Create your views here.

def Home(request):
    return render(request, 'pages/index.html')

def About(request):
    return render(request, 'pages/about.html')

def Contact(request):
    return render(request, 'pages/contact.html')

def ArticleList(request):
    user = request.user
    articlelist = Article.objects.filter(auteur=user)
    return render(request, 'pages/index.html', {"listeArticle": articlelist})