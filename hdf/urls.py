from django.urls import path

from hdf import views

app_name = 'dhf'
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='about'),
]
