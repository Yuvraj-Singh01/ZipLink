from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.loginUser, name = 'login'),
    path('logout/',views.logoutUser, name = 'logout'),
    path('shorten/', views.shorten_url, name = 'shorten_url'),  # Shorten URL logic
    path('userHome/', views.userHome, name='userHome'),
    path('qr-page/', views.qr_page, name='qr_page'),
    path('send/', views.generated_qr, name='generated_qr'),
    path('<str:shortened_id>/', views.redirect_to_original, name = 'redirect_to_original'),  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)