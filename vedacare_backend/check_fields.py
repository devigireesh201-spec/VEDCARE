import os
import sys
import django  # type: ignore

# Add the project root to sys.path to help static analyzers and runtime resolution
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vedacare_backend.settings')
django.setup()

from core.models import AyurvedicPlant  # type: ignore

for field in AyurvedicPlant._meta.get_fields():
    print(f"{field.name}: {type(field)}")
