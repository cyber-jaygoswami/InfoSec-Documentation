from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.homePage,name="homePage"),
    path('about/',views.aboutPage,name="aboutPage"),
    path('content/',views.getContent,name='getContent'),
    path('tool-name/',views.getToolName,name='getToolName'),

]
