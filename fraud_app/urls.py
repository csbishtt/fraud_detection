from django.contrib import admin
from django.urls import path 
from fraud_app import views

urlpatterns = [
    path('',views.index, name='fraud_app'),
    path('prediction',views.prediction,name='prediction'),
    path('features',views.features,name='features'),
    path('about',views.about, name='about'),

]
