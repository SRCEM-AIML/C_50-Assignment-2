from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('latest-news/', views.latest_news, name='latest-news'),
    path('tech-trends/', views.tech_trends, name='tech-trends'),
]
