from django.urls import path, include
# from app import views
from .views import *

urlpatterns = [
    # path('home', home, name="home"),
    # path('emp', emp, name="emp"),
    # path('show', show),
    # path('index', index),
    # path('edit/<int:id>', edit),
    # path('update/<int:id>', update),
    # path('delete/<int:id>', destroy),
    path('blog_by_author/<str:author>', blog_by_author),
    path('new_post', new_post, name="new_post"),
    path('new_post_details/<int:id>', new_post_details, name="new_post_details"),
    path('show_post', show_post, name="show_post"),
    path('show_post/<int:id>', show_post),
    path('edit_post/<int:id>', edit_post, name="edit_post"),
    path('update_post/<int:id>', update_post, name='update_post'),
    path('destroy_post/<int:id>', destroy_post),
    path("register", register_request, name="register"),
    path("login/", login_request, name="login"),
    path("logout", logout_request, name="logout"),
]
