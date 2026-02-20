import re
from .models import AyurvedicCondition

def predict_ayurveda(symptom_text):
    """Predict Ayurvedic condition based on keyword matching from Database."""
    text = symptom_text.lower()
    
    # Get all logic entries from Database
    conditions = AyurvedicCondition.objects.all()
    
    for entry in conditions:
        keywords = [k.strip() for k in entry.keywords.split(',')]
        for word in keywords:
            if word in text:
                return entry.name, entry.remedy, entry.preparation, [t.strip() for t in entry.search_terms.split(',')]
                
    # Default Fallback if no keywords match
    return "General Wellness (Tridoshic)", "Triphala powder with warm water.", "Mix 1 tsp Triphala powder in warm water. Drink at bedtime for overall balance and detoxification.", ["Triphala"]