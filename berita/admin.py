from django.contrib import admin
from berita.models import Kategori, Artikel
# Register your models here.
admin.site.register(Kategori)

class ArtikelAdmin(admin.ModelAdmin):
    list_display = ['judul','Kategori','author']
    search_fields = ['judul']
admin.site.register(Artikel, ArtikelAdmin)