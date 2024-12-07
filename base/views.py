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

def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')  # Redirect if already logged in
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('index')  # Redirect to your home page or dashboard
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def shorten_url(request):
    if request.method == "POST":
        original_url = request.POST.get('url')
        if original_url:
            # Check if the URL is already in the database
            existing_entry = ShortenedURL.objects.filter(original_url=original_url).first()
            if existing_entry:
                shortened_id = existing_entry.shortened_id  # Reuse the existing shortened ID
            else:
                # Create a new ShortenedURL object without a shortened_id
                new_entry = ShortenedURL(original_url=original_url)

                # Save the object first to generate the ID
                new_entry.save()

                # Now the ID has been generated, so we can call encode_to_base62
                shortened_id = encode_to_base62(new_entry.id)

                # Assign the shortened_id to the object
                new_entry.shortened_id = shortened_id

                # Save the object again to store the shortened_id
                new_entry.save()

            # Generate the full shortened URL
            shortened_url = f"www.ziplink.com/{shortened_id}"
            return render(request, 'index.html', {'shortened_url': shortened_url})
        else:
            return render(request, 'index.html', {'error': "Invalid URL"})
    return render(request, 'index.html')

def redirect_to_original(request, shortened_id):
    entry = get_object_or_404(ShortenedURL, shortened_id = shortened_id)
    return HttpResponseRedirect(entry.original_url)

def userHome(request):
    return render(request, 'userHome.html')