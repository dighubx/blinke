from django.urls import path
from . import views

app_name = 'reselling'

urlpatterns = [
    path('', views.reselling_home, name='reselling_home'), 
    path('category/<slug:slug>/', views.category_plans, name='category_detail'),
    path('plan/<slug:slug>/', views.plan_detail, name='plan_detail'),
    path('order/success/', views.order_success, name='order_success'),
]
