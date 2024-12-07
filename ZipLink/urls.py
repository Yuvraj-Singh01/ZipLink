from django.contrib import admin
from django.urls import path, include
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name ='home'),
    path('login/',views.login,name = 'login'),
    path('shorten/',views.shorten_url, name = 'shorten_url'),
     path('api/shorten/', views.shorten_url, name='shorten_url'),  
    path('<str:short_code>/', views.redirect_to_url, name='redirect_url'),
]
