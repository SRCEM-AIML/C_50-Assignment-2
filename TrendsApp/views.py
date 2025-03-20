from django.shortcuts import render

def ai_trends(request):
    return render(request, 'TrendsApp/ai_trends.html')

def blockchain_updates(request):
    return render(request, 'TrendsApp/blockchain_updates.html')
