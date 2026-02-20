from django.db import models
from django.contrib.auth.models import User

# MODULE 1: User Profile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], null=True, blank=True)
    medical_history = models.TextField(blank=True)
    allergies = models.TextField(blank=True)

# MODULE 2: Disease & Symptom Management
class AyurvedicCondition(models.Model):
    name = models.CharField(max_length=200) # e.g. Vata Imbalance
    keywords = models.TextField() # comma-separated keywords: dry, cold, anxious
    remedy = models.TextField()
    preparation = models.TextField()
    search_terms = models.CharField(max_length=255) # for botanical matching

    def __str__(self):
        return self.name

# MODULE 5: Plant & Treatment Database
class AyurvedicPlant(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='plants/')
    medicinal_use = models.TextField()
    properties = models.TextField() # e.g. Rasa, Guna, Virya
    habitat = models.TextField()
    preparation_method = models.TextField()
    precautions = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) # For Module 6

    def __str__(self):
        return self.name

# MODULE 3 & 8: Disease Prediction & History
class HealthReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symptoms_entered = models.TextField()
    predicted_disease = models.CharField(max_length=200)
    remedy = models.TextField(blank=True)
    preparation_method = models.TextField(blank=True)
    probability = models.FloatField() # Severity/Probability %
    created_at = models.DateTimeField(auto_now_add=True)
    recommended_plants = models.ManyToManyField(AyurvedicPlant)

# MODULE 6: E-Kart (Simple Order Model)
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(AyurvedicPlant)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Packed') # Shipped, Delivered
    ordered_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(null=True, blank=True)
    review = models.TextField(null=True, blank=True)

# MODULE 9: Notifications
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default="New Notification")
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.title}"