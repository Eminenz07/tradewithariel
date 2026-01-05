from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MentorshipCard, Product, AboutSection, SiteSettings
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def admin_login(request):
    if request.method == 'POST':
        # Simple login logic or use Django's auth forms
        from django.contrib.auth.forms import AuthenticationForm
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        from django.contrib.auth.forms import AuthenticationForm
        form = AuthenticationForm()
    return render(request, 'cms/login.html', {'form': form})

def admin_logout(request):
    logout(request)
    return redirect('admin_login')

@login_required
def dashboard(request):
    mentorship_count = MentorshipCard.objects.count()
    product_count = Product.objects.count()
    return render(request, 'cms/dashboard.html', {
        'mentorship_count': mentorship_count,
        'product_count': product_count
    })

@login_required
def mentorship_list(request):
    cards = MentorshipCard.objects.all()
    return render(request, 'cms/mentorship_list.html', {'cards': cards})

# Placeholder wrappers for editing - in real scenario would use Forms
@login_required
def mentorship_edit(request, pk):
    card = get_object_or_404(MentorshipCard, pk=pk)
    if request.method == 'POST':
        card.title = request.POST.get('title')
        card.destination_link = request.POST.get('destination_link')
        card.description = request.POST.get('description')
        if request.FILES.get('image'):
            card.image = request.FILES.get('image')
        
        # Checkbox handling
        card.is_active = request.POST.get('is_active') == 'on'
        
        card.save()
        messages.success(request, "Mentorship card updated.")
        return redirect('mentorship_list')
    return render(request, 'cms/mentorship_form.html', {'card': card})

@login_required
def mentorship_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        link = request.POST.get('destination_link')
        desc = request.POST.get('description')
        image = request.FILES.get('image')
        MentorshipCard.objects.create(title=title, destination_link=link, description=desc, image=image)
        messages.success(request, "Mentorship card created.")
        return redirect('mentorship_list')
    return render(request, 'cms/mentorship_form.html')

@login_required
def mentorship_disable(request, pk):
    card = get_object_or_404(MentorshipCard, pk=pk)
    card.is_active = not card.is_active
    card.save()
    status = "enabled" if card.is_active else "disabled"
    messages.success(request, f"Card {status}.")
    return redirect('mentorship_list')

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'cms/product_list.html', {'products': products})

@login_required
def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        is_active = request.POST.get('is_active') == 'on'
        image = request.FILES.get('image')
        
        Product.objects.create(
            name=name, price=price, description=description, 
            is_active=is_active, image=image
        )
        messages.success(request, "Product created successfully.")
        return redirect('product_list')
    return render(request, 'cms/product_form.html')

@login_required
def product_disable(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.is_active = not product.is_active
    product.save()
    status = "enabled" if product.is_active else "disabled"
    messages.success(request, f"Product {status}.")
    return redirect('product_list')

@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')
        product.is_active = request.POST.get('is_active') == 'on'
        if request.FILES.get('image'):
            product.image = request.FILES.get('image')
        product.save()
        messages.success(request, "Product updated.")
        return redirect('product_list')
    return render(request, 'cms/product_form.html', {'product': product})

@login_required
def about_edit(request):
    about = AboutSection.objects.first()
    if not about:
        about = AboutSection.objects.create(title="About Ariel", content="Content here...")
    
    if request.method == 'POST':
        about.title = request.POST.get('title')
        about.content = request.POST.get('content')
        if request.FILES.get('image'):
            about.image = request.FILES.get('image')
        about.save()
        messages.success(request, "About section updated.")
        return redirect('dashboard')
    return render(request, 'cms/about_form.html', {'about': about})

@login_required
def settings_edit(request):
    settings = SiteSettings.load()
    if request.method == 'POST':
        settings.contact_email = request.POST.get('contact_email')
        settings.save()
        messages.success(request, "Site settings updated.")
        return redirect('dashboard')
    return render(request, 'cms/settings_form.html', {'settings': settings})
