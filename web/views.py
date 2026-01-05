from django.shortcuts import render, redirect
from cms.models import MentorshipCard, Product, AboutSection, SiteSettings
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        sender_email = request.POST.get('email')
        message_body = request.POST.get('message')
        
        # Get dynamic receiver
        site_settings = SiteSettings.load()
        recipient_list = [site_settings.contact_email]
        
        subject = f"New Contact from {name} - TradeWithAriel"
        full_message = f"Sender: {name} <{sender_email}>\n\nMessage:\n{message_body}"
        
        try:
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@tradewithariel.com',
                recipient_list,
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully.")
        except Exception as e:
            # Check console for the email in dev mode
            print(f"Email Error: {e}")
            messages.error(request, "Failed to send message. Please try again.")
            
        return redirect('index')

    mentorship_cards = MentorshipCard.objects.filter(is_active=True)
    products = Product.objects.filter(is_active=True)
    about_section = AboutSection.objects.first()
    
    import os
    hero_images = []
    hero_dir = os.path.join(settings.BASE_DIR, 'static', 'images', 'hero')
    if os.path.exists(hero_dir):
        hero_images = [f'images/hero/{f}' for f in os.listdir(hero_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        hero_images = hero_images[:15]

    context = {
        'mentorship_cards': mentorship_cards,
        'products': products,
        'about_section': about_section,
        'hero_images': hero_images,
    }
    return render(request, 'web/index.html', context)
