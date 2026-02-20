from django.contrib import admin
from .models import UserProfile, AyurvedicPlant, HealthReport, Order, Notification

admin.site.register(UserProfile)
admin.site.register(AyurvedicPlant)
admin.site.register(HealthReport)
admin.site.register(Order)
admin.site.register(Notification)