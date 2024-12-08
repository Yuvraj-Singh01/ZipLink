from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.loginUser, name = 'login'),
    path('logout/',views.logoutUser, name = 'logout'),
    path('shorten/', views.shorten_url, name = 'shorten_url'),  # Shorten URL logic
    path('userHome/', views.userHome, name='userHome'),
    path('<str:shortened_id>/', views.redirect_to_original, name = 'redirect_to_original'),  # Redirect to original URL 
]