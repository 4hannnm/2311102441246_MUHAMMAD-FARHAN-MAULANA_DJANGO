from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import home, about, contact, detail_artikel

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('detail/<slug:slug>', detail_artikel, name="detail_artikel"),
    path('dashboard/', include("berita.urls"))
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)