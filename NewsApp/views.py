from django.shortcuts import render

def homepage(request):
    return render(request, 'NewsApp/homepage.html')

def latest_news(request):
    return render(request, 'NewsApp/latest_news.html')

def tech_trends(request):
    return render(request, 'NewsApp/tech_trends.html')
