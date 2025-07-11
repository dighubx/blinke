from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import Contact
from .models import JobOpening
from .models import Product, Category
from .models import Inquiry


def landing_page(request):
    return render(request, 'core/home.html')

def acronis_backup_view(request):
    features = [
        'AI-Based Threat Detection',
        'Bare-metal Recovery',
        'Cloud Console Access',
        'AES-256 Encryption',
        'Real-Time Backup Sync',
        'Multiple OS Support',
    ]

    plans = [
        ('Starter', '₹499/mo', '100GB Cloud'),
        ('Business', '₹1,299/mo', '500GB + Local Option'),
        ('Enterprise', '₹2,499/mo', '1TB + Advanced AI & Ransomware Protection'),
    ]

    return render(request, 'core/acronis.html', {
        'features': features,
        'plans': plans,
    })

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            messages.success(request, "Your message has been sent!")
            return redirect('contact')
        else:
            messages.error(request, "All fields are required.")

    return render(request, 'core/contact.html')


def terms_of_service(request):
    return render(request, 'core/terms.html')

def privacy_policy(request):
    return render(request, 'core/privacy.html')

def refund_policy(request):
    return render(request, 'core/refund.html')

def about_us(request):
    return render(request, 'core/about.html')   



def careers(request):
    jobs = JobOpening.objects.filter(is_active=True).order_by('-posted_on')
    return render(request, 'core/career.html', {'jobs': jobs})



def backup_plans(request):
    category_slug = request.GET.get('category')
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_active=True)
        selected_category = category_slug
    else:
        products = Product.objects.filter(is_active=True)
        selected_category = None

    return render(request, 'core/backup_plans.html', {
        'products': products,
        'categories': categories,
        'selected_category': selected_category
    })


def category_products_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.product_set.filter(is_active=True)
    return render(request, 'core/category_products.html', {
        'category': category,
        'products': products
    })



def submit_inquiry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        message = request.POST.get('message')

        if name and email and service:
            Inquiry.objects.create(
                name=name,
                email=email,
                phone=phone,
                service=service,
                message=message
            )
            messages.success(request, "Your inquiry has been submitted successfully!")
            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            messages.error(request, "Please fill in all required fields.")
            return redirect(request.META.get('HTTP_REFERER', '/'))

    return redirect('/')