from django.urls import path
from .views import*
from . import views
from .views import acronis_backup_view

urlpatterns = [
    path('', landing_page, name='home'),
    path('contact/', contact_view, name='contact'),
    path('terms-of-service/', views.terms_of_service, name='terms'),
    path('privacy-policy/', views.privacy_policy, name='privacy'),
    path('refund-policy/', views.refund_policy, name='refund'),
    path('about/', views.about_us, name='about'),
    path('careers/', views.careers, name='careers'),
    path('backup-plans/', views.backup_plans, name='backup_plans'),
    path('backup/<slug:slug>/', views.category_products_view, name='category_products'),
    path('submit-inquiry/', views.submit_inquiry, name='submit_inquiry'),
    path('acronis-backup/', acronis_backup_view, name='acronis_backup'),


]