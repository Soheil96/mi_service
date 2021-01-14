from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contactus/', views.contactus, name='contactus'),
    path('inquiry/', views.inquiry, name='inquiry'),
    path('inquiry/result/', views.result, name='result'),
    path('termsofservice/', views.termsofservice, name='termsofservice'),
]
