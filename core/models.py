from django.db import models

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
