from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', landing_page, name='home'),
    path('contact/', contact_view, name='contact'),
    path('terms-of-service/', views.terms_of_service, name='terms'),
    path('privacy-policy/', views.privacy_policy, name='privacy'),
    path('refund-policy/', views.refund_policy, name='refund'),
    path('about/', views.about_us, name='about'),
     path('careers/', views.careers, name='careers'),

]