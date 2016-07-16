from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^email/', views.email, name='email'),
    url(r'^error/', views.error, name='error')
]
