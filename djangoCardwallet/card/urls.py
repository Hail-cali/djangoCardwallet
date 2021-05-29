#card/urls.py
from django.urls import path
from cardwallet import views

urlpatterns = [
    path('', views.Post, name='mycard'),
    path('/discover', views.Uploads, name='discover'),
    path('/cash',views.Fillcash, name ='cash'),
    path('/del',views.deletecard, name ='del'),
    path('/create', views.createcard, name ='create'),
]