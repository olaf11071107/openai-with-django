from django.urls import path 
from openapp import views


urlpatterns=[
    path("", views.HomeView.as_view(), name='main'),
    path("sign-up/", views.SignUp.as_view(), name='signup'),
    path("delete/", views.DeleteHistory, name='deleteChat'),
    path("logout/", views.logout_view, name="logout"),
    path("login/", views.LoginView.as_view(), name="login"),
]