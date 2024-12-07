from django.shortcuts import render, redirect, get_object_or_404    
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import ShortenedURL
from .utils import encode_to_base62

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request,'login.html')

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