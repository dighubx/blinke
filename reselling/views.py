from django.shortcuts import render , redirect
from django.shortcuts import render, get_object_or_404
from .models import ServiceCategory, ServicePlan
from .models import ServiceCategory, ServicePlan, Testimonial, HomeCTA
from .models import ServicePlan
from .forms import OrderForm

def reselling_home(request):
    categories = ServiceCategory.objects.all()[:6]
    featured_plans = ServicePlan.objects.filter(is_active=True)[:6]
    testimonials = Testimonial.objects.filter(is_active=True)[:3]
    cta = HomeCTA.objects.filter(is_active=True).first()  # 🔥 This line matters

    return render(request, 'reselling/reselling_home.html', {
        'categories': categories,
        'featured_plans': featured_plans,
        'testimonials': testimonials,
        'cta': cta,  # 🔥 This too
    })

def category_plans(request, slug):
    category = get_object_or_404(ServiceCategory, slug=slug)
    plans = category.plans.filter(is_active=True)
    return render(request, 'reselling/plan_list.html', {'category': category, 'plans': plans})


def reselling_home(request):
    categories = ServiceCategory.objects.all()[:6]
    featured_plans = ServicePlan.objects.filter(is_active=True)[:6]
    testimonials = Testimonial.objects.filter(is_active=True)[:3]

    return render(request, 'reselling/reselling_home.html', {
        'categories': categories,
        'featured_plans': featured_plans,
        'testimonials': testimonials
    })





def plan_detail(request, slug):
    plan = get_object_or_404(ServicePlan, slug=slug)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.plan = plan
            order.user = request.user if request.user.is_authenticated else None
            order.save()
            return redirect('reselling:order_success')
    else:
        form = OrderForm()

    return render(request, 'reselling/plan_detail.html', {
        'plan': plan,
        'form': form
    })


def order_success(request):
    return render(request, 'reselling/order_success.html')