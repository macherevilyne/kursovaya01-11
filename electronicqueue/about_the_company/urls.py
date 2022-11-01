from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.about_the_company, name='about_the_company'),

]
