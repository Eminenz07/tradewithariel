from django.db import models

class MentorshipCard(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    destination_link = models.URLField(help_text="Where this card links to (e.g. WhatsApp, Telegram)")
    image = models.ImageField(upload_to='mentorship_images/', blank=True, null=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class AboutSection(models.Model):
    title = models.CharField(max_length=200, default="About Ariel")
    content = models.TextField(help_text="Main text content for the About section")
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class SiteSettings(models.Model):
    contact_email = models.EmailField(default='tradewithariel@gmail.com')
    
    def __str__(self):
        return "Site Settings"

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
