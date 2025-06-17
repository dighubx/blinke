from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from .models import JobOpening


def landing_page(request):
    return render(request, 'core/home.html')

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
