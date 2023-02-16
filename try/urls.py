from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about-us/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('our-blogs/', views.blog, name='blog')
]
