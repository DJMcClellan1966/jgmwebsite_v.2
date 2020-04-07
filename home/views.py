from django.shortcuts import render

def terms(request):
    return render(request, 'jobs/terms.html')

def privacy(request):
    return render(request, 'jobs/privacy.html')

def home(request):
    return render(request, 'jobs/home.html')
