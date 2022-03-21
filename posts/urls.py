from django.urls import path

from .views import Home, About, Contact, ArticleList
urlpatterns = [
    path("", Home, name='index'),
    path("about/", About, name='about'),
    path("contact/", Contact, name='contact'),
    path("contactlist/", ArticleList, name='index')
]
