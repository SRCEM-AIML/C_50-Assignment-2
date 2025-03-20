from django.urls import path
from . import views

urlpatterns = [
    path('ai-trends/', views.ai_trends, name='ai-trends'),
    path('blockchain-updates/', views.blockchain_updates, name='blockchain-updates'),
]
