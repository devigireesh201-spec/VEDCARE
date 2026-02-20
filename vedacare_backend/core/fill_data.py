import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vedacare_backend.settings')
django.setup()

from core.models import AyurvedicPlant

plants = [
    {
        "name": "Ashwagandha", 
        "sci": "Withania somnifera", 
        "use": "Reduces stress and anxiety. Good for Vata imbalance.",
        "price": 250.00
    },
    {
        "name": "Tulsi", 
        "sci": "Ocimum sanctum", 
        "use": "Treats cough, cold, and respiratory issues. Balances Kapha.",
        "price": 150.00
    },
]

for p in plants:
    AyurvedicPlant.objects.get_or_create(
        name=p['name'],
        scientific_name=p['sci'],
        medicinal_use=p['use'],
        price=p['price']
    )
print("✅ Database populated with basic herbs!")