from django.urls import path
from berita.views import dashboard

urlpatterns = [
    path('', dashboard, name= "dashboard"),

]

