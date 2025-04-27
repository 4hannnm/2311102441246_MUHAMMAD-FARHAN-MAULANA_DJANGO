# 2311102441246_MUHAMMAD-FARHAN-MAULANA-DJANGO

# Personal Portfolio

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![Django](https://img.shields.io/badge/Django-%23092E20.svg?logo=django&logoColor=white)](#)


## Deskripsi Singkat
Membuat CRUD untuk kategori dan artikel. Mengubah templates yang ada di dashboard menjadi apa yang telah kita buat di admin

## Ada apa saja di website ini
1. membuat CRUD kategori
2. membuat CRUD artikel


# Cara menjalankan project
1. salin projek
```
git clone https://github.com/4hannnm/2311102441246_MUHAMMAD-FARHAN-MAULANA_DJANGO
```
2. Aktifkan .venv 
```
.venv\Scripts\activate
```
3. mulai server
```
py manage.py runserver
```
4. Jika server sudah jalan maka akan muncul halaman website

5. jika ingin pindah ke dashbord
```
http://127.0.0.1:8000/dashboard/
```

6. CRUD Kategori di views.py
```
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
```

7. CRUD Artikel di views.py
```
def artikel_list(request) : 
    template_name = "dashboard/snippets/artikel_list.html"
    artikel = Artikel.objects.all()
    print(artikel)
    context = {
        'title' : 'daftarartikel',
        'artikel' : artikel
    }
    return render(request, template_name, context)

def artikel_add(request):
    template_name = "dashboard/snippets/artikel_forms.html"
    if request.method == "POST":
        forms = ArtikelForm(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.author = request.user
            pub.save()
            return redirect(artikel_list)
        else:
            print(forms.errors)
            
    forms = ArtikelForm()
    context = {
        'title' : 'tambah artikel',
        'forms' : forms
    }
    return render(request, template_name, context)

def artikel_detail(request, id_artikel):
    template_name = "dashboard/snippets/artikel_detail.html"
    artikel = Artikel.objects.get(id= id_artikel)
    context = {
        'title' : artikel.judul,
        'artikel' : artikel
    }
    return render(request, template_name, context)

def artikel_update(request, id_artikel):
    template_name = "dashboard/snippets/artikel_forms.html"
    artikel = Artikel.objects.get(id=id_artikel)
    if request.method == "POST":
        forms = ArtikelForm(request.POST, request.FILES, instance=artikel)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.author = request.user
            pub.save()
            return redirect(artikel_list)
            
    forms = ArtikelForm(instance=artikel)
    context = {
        'title' : 'tambah kategori',
        'forms' : forms
    }
    return render(request, template_name, context)

def artikel_delete(request, id_artikel):
    try:
        Artikel.objects.get(id=id_artikel).delete()
    except:pass
    return redirect(artikel_list)
```