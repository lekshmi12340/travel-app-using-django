from django.urls import path
from . import views

urlpatterns=[path('home',views.home),
            path('about',views.about),
             path('blog',views.blog),
             path('contact', views.contact),
             path('destination_details', views.destination_details),
             path('elements', views.elements),
             path('index', views.index),
             path('main', views.main),
             path('singleblog', views.singleblog),
             path('travel_destination', views.travel_destination),
             path('index', views.index),
             path('mailsending', views.mailsending),
             path('signup',views.signup),
             path('subscribe',views.subscribe),
             path('destiny',views.destiny),
             path('login', views.login),
             path('breply', views.breply),
             path('joindetails', views.joindetails),
             path('loginn', views.loginn),
             path('availability', views.availability),
             ]