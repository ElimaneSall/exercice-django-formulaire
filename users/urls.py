from django.urls import path

from . import views

urlpatterns = [
    path('',  views.index, name="index"),
    path('formprof', views.formprof, name="formprof" ),
    path('formprof2', views.formprof2, name="formprof2" ),
]