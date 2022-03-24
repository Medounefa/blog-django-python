from django.urls import include, path

from .views import Home, About, Contact, ArticleList, BlogList, newBlog, detailsBlog, editBlog, deleteBlog
urlpatterns = [
    path("", ArticleList, name='homeblog'),
    path("about/", About, name='about'),
    path("contact/", Contact, name='contact'),
    path("homeblog/", ArticleList, name='homeblog'),
    path("allblog/", BlogList, name='allblog'),
    path("newblog/", newBlog, name='newblog'),
    path("allblog/<int:id>/", detailsBlog, name='detailsblog'),
    path("allblog/edit/<int:id>/", editBlog, name='editblog'),
    path("allblog/delete/<int:id>/", deleteBlog, name='deleteblog')
]
