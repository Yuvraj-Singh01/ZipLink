from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ShortenedURL

# Create your views here.
def index(request):

    return render(request, 'index.html')

def login(request):
    return render(request,'login.html')

def shorten_url(request):
    if request.method == "POST":
        original_url = request.POST.get('url')
        if original_url:
            # Simulate URL shortening logic
            shortened_url = "www.ziplink.xDnwi12"  # Replace with actual logic
            return render(request, 'index.html', {'shortened_url': shortened_url})
        else:
            return render(request, 'index.html', {'error': "Invalid URL"})
    return render(request, 'index.html')