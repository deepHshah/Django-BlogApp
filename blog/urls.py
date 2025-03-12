from django.urls import path
from .views import *

urlpatterns=[
    path('main/',main,name='main'),
    path('',home,name="home"),
    path('login/',Login,name="login"),
    path('register/',register,name="register"),
    path("logout/",signout,name="logout"),
    path("addblog/",addblog,name="addblog"),
    path("profile/",Profile,name="profile"),
    path('edit/<int:blog_id>/', edit_blog, name='edit_blog'),

]