from django.db import models
from django.utils.text import slugify
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class JobOpening(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    description = models.TextField()
    apply_link = models.URLField()
    is_active = models.BooleanField(default=True)
    posted_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name    


class Inquiry(models.Model):
    SERVICE_CHOICES = [
        ("AI & ML Development", "AI & ML Development"),
        ("Web & Mobile Apps", "Web & Mobile Apps"),
        ("Backup Solutions", "Backup Solutions"),
        ("Custom Software", "Custom Software"),
        ("Cloud Solutions", "Cloud Solutions"),
        ("Cybersecurity", "Cybersecurity"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service}"       