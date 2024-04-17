from django.urls import path
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('index', index, name='index'),
    path('add_art', add_art, name='add_art'),
    path('search_page', search_page, name='search_page'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('my_arts', my_arts, name='my_arts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
