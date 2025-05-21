from django.shortcuts import render
from berita.models import Artikel, Kategori

def home(request, kategori=None):
    template_name = "halaman/index.html"
    kategori = request.GET.get('kategori')
    if kategori == None:
        print("ALL")
        data_artikel = Artikel.objects.all()
        menu_aktif = "ALL"
    else:
        print("bukan ALL")    
        get_kategori = Kategori.objects.filter(nama=kategori)
        print(get_kategori)
        if get_kategori.count() != 0:
            data_artikel = Artikel.objects.filter(kategori=get_kategori[0])
            menu_aktif = kategori
        else:
            menu_aktif = "ALL"
            data_artikel = []
                
    data_kategori = Kategori.objects.all()
    context = {
        'title' : 'my home',
        'welcome' : 'welcome my home',
        'data_artikel' : data_artikel,
        'data_kategori' : data_kategori,
        'menu_aktif' : menu_aktif
    }
    return render(request, template_name, context)

def about(request):
    template_name = "halaman/about.html"
    context = {
        'title' : 'about me',
        'welcome' :'ini page about me',
    }
    return render(request, template_name, context)

def contact(request):
    template_name = "halaman/contact.html"
    context = {
        'title' : 'about me',
        'welcome' :'ini page about me',
    }
    return render(request, template_name, context)

def detail_artikel(request, slug):
    template_name = "halaman/detail_artikel.html"
    artikel = Artikel.objects.get(slug=slug)
    context = {
        'title' : artikel.judul,
        'artikel' : artikel,
    }
    return render(request, template_name, context)