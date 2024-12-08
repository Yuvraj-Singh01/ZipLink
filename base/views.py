from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import ShortenedURL
from .utils import encode_to_base62

# Create your views here.

def index(request):
    return render(request, 'index.html')


def loginUser(request):
    user=None
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('new-password')
        print(username,password)
        user = authenticate(username=username, password=password)
    if user is not None:
        print("Bao")
        login(request, user)
        return redirect("userHome")
    else:
        messages.error(request, "Wrong username or password. Please try again.")
        return render(request, 'login.html')
    
def logoutUser(request):
    logout(request)
    return redirect(reverse_lazy("index"))

def userHome(request):
    return render(request, 'userHome.html')

def shorten_url(request):
    if request.method == "POST":
        original_url = request.POST.get('url')
        if original_url:
            # Check if the URL already exists
            entry, created = ShortenedURL.objects.get_or_create(original_url=original_url)
            if created:
                entry.shortened_id = encode_to_base62(entry.id)
                entry.save()

            # Construct the shortened URL
            base_url = request.build_absolute_uri('/')  # Gets the base URL (e.g., http://127.0.0.1:8000/)
            shortened_url = f"{base_url}{entry.shortened_id}/"
            return render(request, 'index.html', {'shortened_url': shortened_url})
        else:
            return render(request, 'index.html', {'error': "Invalid URL"})
    return render(request, 'index.html')


def redirect_to_original(request, shortened_id):
    entry = get_object_or_404(ShortenedURL, shortened_id=shortened_id)
    return HttpResponseRedirect(entry.original_url)

def userHome(request):
    return render(request, 'userHome.html')