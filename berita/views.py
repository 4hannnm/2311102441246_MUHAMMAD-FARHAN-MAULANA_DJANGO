from django.shortcuts import render, redirect
from berita.models import Kategori, Artikel

# Create your views here.

def dashboard(request):
    template_name = "dashboard/index.html"
    context = {
        'title' : 'halaman dashboard'
    }
    return render(request, template_name, context)

def kategori_list(request):
    template_name = "dashboard/snippets/kategori_list.html"
    kategori = Kategori.objects.all()
    print(kategori)
    context = {
        'title' : 'halaman kategori',
        'kategori' : kategori,
     }
    return render(request, template_name, context)

def kategori_add(request):
    template_name = "dashboard/snippets/kategori_add.html"
    if request.method == "POST":
        nama_input = request.POST.get('nama_kategori')
        print(nama_input)
        Kategori.objects.create(
            nama = nama_input
        )
        return redirect(kategori_list)

        
    context = {
        'title' : 'tambah kategori',
    }
    return render(request, template_name, context)

def kategori_update(request , id_kategori):
    template_name = "dashboard/snippets/kategori_update.html"
    try:
        kategori = Kategori.objects.get(id=id_kategori)
    except:
        return redirect(kategori_list)
    
    if request.method == "POST":
        nama_input = request.POST.get('nama_kategori')
        kategori.nama = nama_input
        kategori.save()
        return redirect(kategori_list)
    context = {
        'title' : 'tambah kategori',
        'kategori' : kategori
    }
    return render(request, template_name, context)

def kategori_delete(request, id_kategori):
    try:
        Kategori.objects.get(id=id_kategori).delete()
    except:
        pass
    return redirect(kategori_list)