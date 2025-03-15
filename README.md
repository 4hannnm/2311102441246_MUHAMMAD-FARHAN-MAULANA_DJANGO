# 2311102441246_MUHAMMAD-FARHAN-MAULANA-DJANGO

# Personal Portfolio

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![Django](https://img.shields.io/badge/Django-%23092E20.svg?logo=django&logoColor=white)](#)


## Deskripsi Singkat
Membuat model di django

## Ada apa saja di website ini
1. membuat model pengguna
2. membuat model berita


# Cara menjalankan project
1. salin projek
```
git clone https://github.com/4hannnm/2311102441246_MUHAMMAD-FARHAN-MAULANA_DJANGO
```
2. Aktifkan .venv 
```
.venv\Scripts\activate
```
3. membuat apps pengguna
```
py manage.py startapp pengguna
```

4. membuat apps berita
```
py manage.py startapp berita
```

5. membuat model pengguna/models.py
```
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Biodata(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    alamat = models.TextField(blank=True, null=True)
    telpon = models.CharField(max_length=20, blank=True, null=True)
    foto = models.ImageField(upload_to='pengguna', blank=True, null=True)

    def _str_(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = "1. Biodata"
```

6. membuat model berita/models.py
```
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Kategori(models.Model):
    nama = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = "1. Kategori"
            
class Artikel(models.Model):
    judul = models.CharField(max_length=255)
    isi = models.TextField(blank=True, null=True)
    Kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    thumbnail = models.ImageField(upload_to='artikel',blank=True, null=True)
    
    def __str__(self):
        return self.judul
    
    class Meta:
        verbose_name_plural = "2. Artikel"
```

7. Setelah project dan apps telah dibuat dan untuk mengeceknya kita bisa mengetik
```
py manage.py runserver
```