import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from cms.models import MentorshipCard, Product, AboutSection

def create_data():
    # Create Superuser
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
        print("Superuser 'admin' created.")

    # Create Mentorship Cards
    if not MentorshipCard.objects.exists():
        MentorshipCard.objects.create(
            title="Join Trading Journal",
            description="Daily market analysis and setups.",
            destination_link="https://t.me/example",
            order=1
        )
        MentorshipCard.objects.create(
            title="Nigerian Stock Class",
            description="Learn local market dynamics.",
            destination_link="https://example.com/class",
            order=2
        )
        print("Mentorship cards created.")

    # Create Products
    if not Product.objects.exists():
        Product.objects.create(
            name="Prop Firm Pass",
            description="Discounted access to top firms.",
            price=99.99
        )
        print("Products created.")

    # Create About Section
    if not AboutSection.objects.exists():
        AboutSection.objects.create(
            title="Who is Ariel?",
            content="Ariel is a professional trader with over 5 years of experience in forex and commodities..."
        )
        print("About section created.")

if __name__ == '__main__':
    create_data()
