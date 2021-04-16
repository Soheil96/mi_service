from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contactus/', views.contact_us, name='contactus'),
    path('inquiry/', views.inquiry, name='inquiry'),
    path('inquiry/result/', views.result, name='result'),
    path('inquiry/result_1/', views.result_1, name='result_1'),
    path('termsofservice/', views.terms_of_service, name='termsofservice'),
    path('manager/', views.manager, name='manager'),
    path('manager/add/', views.add_warranty, name='addwarranty'),
]
