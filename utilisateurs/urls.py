


from django.urls import path
from .views import SignIn, register_user,profile
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path("login/", SignIn, name="login"),
    path("signup/", register_user, name="signup"),
    path("profil/", profile, name='profil'),
    path("logout/", LogoutView.as_view(), name="logout"),
]
