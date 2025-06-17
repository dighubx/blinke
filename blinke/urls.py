from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
     path('accounts/', include('accounts.urls')),  # Custom URLs
    path('accounts/', include('allauth.urls')),   # Allauth social login
]
