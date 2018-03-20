from django.urls import path

from hdf import views

app_name = 'hdf'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('agents/', views.agents, name='agents'),
    path('sale/', views.for_sale, name='sale'),
    path('rent/', views.for_rent, name='rent'),
    path('price/', views.pricing, name='price'),
    path('faqs/', views.faqs, name='faqs'),
    path('idxpress/', views.idx_press, name='idxpress'),
    path('terms/', views.terms_of_use, name='terms'),
    path('privacy/', views.privacy_policy, name='privacy')
]
