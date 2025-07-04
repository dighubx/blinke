from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# 🔹 Category like Hosting, Domains, SSL, etc.
class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(ServiceCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

# 🔹 Each Plan under a category
class ServicePlan(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='plans')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.TextField(blank=True, help_text="You can use HTML or line breaks for features")
    provider_name = models.CharField(max_length=100, blank=True)
    provider_plan_code = models.CharField(max_length=100, blank=True)
    buying_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(ServicePlan, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - ₹{self.price}"

# 🔹 When user places an order
class ResellOrder(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    plan = models.ForeignKey(ServicePlan, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.plan.title} - {self.payment_status}"




class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} – {self.designation}"
    


class HomeCTA(models.Model):
    heading = models.CharField(max_length=200)
    subtext = models.TextField(blank=True)
    button_text = models.CharField(max_length=100, default="Contact Us")
    button_url = models.URLField(default="/contact/")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.heading