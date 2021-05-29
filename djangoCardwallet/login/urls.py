#login/urls.py
from django.urls import path
from cardwallet import views
from django.conf.urls import url
urlpatterns = [
    #path('', views.Login, name='login'),
    path('/join', views.signup, name='join'),
    path('', views.signin, name='login'),
]