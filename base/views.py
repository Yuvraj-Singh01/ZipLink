from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from .models import ShortenedURL
import base64


BASE_DOMAIN = "http://127.0.0.1:8000/"

# Create your views here.
def index(request):

    return render(request, 'index.html')

def login(request):
    return render(request,'login.html')

def encode_id(id):
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(characters)
    encoded = ""

    while id > 0:
        encoded = characters[id % base] + encoded
        id //=  base
    return encoded

def shorten_url(request):
    if request.method == "POST":
        original_url = request.POST.get('url')
        if not original_url:
            return render(request, 'index.html',{'error': "Inavlid URL"})

        existing_url = ShortenedURL.objects.filter(original_url=original_url).first()
       
        if existing_url:
            short_code = existing_url.shortened_id
        else:

            url_obj = ShortenedURL.objects.create(original_url = original_url)
            short_code = encode_id(url_obj.id)
            url_obj.shortened_id = short_code
            url_obj.save()

    return render(request, 'index.html', {'shortened_url': BASE_DOMAIN + short_code})


def redirect_to_url(request, short_code):
    url_obj = get_object_or_404(ShortenedURL, shortened_id = short_code)
    return redirect(url_obj.original_url)
