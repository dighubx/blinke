from django.contrib import admin
from .models import ServiceCategory, ServicePlan, ResellOrder

from .models import Testimonial

admin.site.register(ServiceCategory)
admin.site.register(ServicePlan)
admin.site.register(ResellOrder)




@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'designation', 'message')


from .models import HomeCTA

@admin.register(HomeCTA)
class HomeCTAAdmin(admin.ModelAdmin):
    list_display = ('heading', 'button_text', 'is_active')