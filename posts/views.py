from datetime import date
import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from posts.models import Article

# Create your views here.

def Home(request):
    return render(request, 'pages/index.html')

def About(request):
    return render(request, 'pages/about.html')

def Contact(request):
    return render(request, 'pages/contact.html')


def ArticleList(request):
    user= request.user
    articlelist = Article.objects.all()
    return render(request, 'pages/index.html', {"listeArticle": articlelist})


def BlogList(request):
    user = request.user
    bloglist = Article.objects.all()
    return render(request, 'blogs/allBlog.html', {"listeBlog": bloglist})


def newBlog(request) :
    if request.method == "POST" :
        auteur = request.user
        titre = request.POST['titre']
        resume = request.POST['resume']
        miniature = request.POST['miniature']
        contenu = request.POST['contenu']
        dateCreation = request.POST['dateCreation']
        newB = Article.objects.create(
            auteur = auteur,
            titre = titre,
            resume = resume,
            miniature =  miniature,
            contenu = contenu ,
            dateCreation = dateCreation
        )
        newB.save()
        return redirect('/allblog/')
    return render(request, "blogs/newBlog.html" )

def detailsBlog(request, id) :
    article = get_object_or_404(Article, id=id)
    return render(request, "blogs/detailsBlog.html", {"article":  article })

def editBlog(request, id) :
    editarticle = get_object_or_404(Article, id=id)
    if request.method == "POST" :
        titre = request.POST['titre']
        resume = request.POST['resume']
        miniature = request.POST['miniature']
        contenu = request.POST['contenu']
        dateModification = request.POST['dateModification']
        editB = Article.objects.filter(pk=editarticle.id)
        editB.update(
            titre = titre,
            resume = resume,
            miniature =  miniature,
            contenu = contenu ,
            dateModification = dateModification
        )
        return redirect('/allblog/')
    return render(request, "blogs/editBlog.html", {"article": editarticle})   

def deleteBlog(request, id) :
    blog = get_object_or_404(Article, id=id)
    if request.method == "POST":
        blog_to_delete =  Article.objects.filter(pk= blog.id)
        blog_to_delete.delete()
     
       
        return redirect("/allblog/")
    return render(request, "blogs/deleteBlog.html", {"blog":  blog})  


