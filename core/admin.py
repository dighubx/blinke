from django.contrib import admin

# Register your models here.

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