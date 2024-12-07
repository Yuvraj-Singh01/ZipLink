from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),  # Homepage
    path('login/', views.login, name = 'login'),  # Login page
    path('shorten/', views.shorten_url, name = 'shorten_url'),  # Shorten URL logic
    path('<str:shortened_id>/', views.redirect_to_original, name = 'redirect_to_original'),  # Redirect to original URL
]