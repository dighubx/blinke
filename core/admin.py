from django.contrib import admin
from .models import Product, Category
# Register your models here.
from .models import Inquiry
from .models import Contact

from .models import JobOpening

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')

@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'experience', 'is_active', 'posted_on')
    list_filter = ('is_active', 'location')
    search_fields = ('title', 'description')    


admin.site.site_header = "Blinke Admin"
admin.site.site_title = "Blinke Technologies"
admin.site.index_title = "Welcome to Blinke Dashboard"   



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'description')



@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'service', 'submitted_at']
    search_fields = ['name', 'email', 'service']    
