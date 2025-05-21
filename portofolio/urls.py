from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from portofolio.views import home, about, contact, detail_artikel
from portofolio.authentication import sign_in, sign_up, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('detail/<slug:slug>', detail_artikel, name="detail_artikel"),
    path('dashboard/', include("berita.urls")),
    
    path('authentication/sign_in', sign_in, name='sign_in'),
    path('authentication/signup', sign_up, name='sign_up'),
    path('authentication/login', user_logout, name='user_logout'),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)