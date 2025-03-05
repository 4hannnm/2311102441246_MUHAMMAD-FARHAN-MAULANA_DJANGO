# 2311102441246_MUHAMMAD-FARHAN-MAULANA-DJANGO

## Deskripsi Singkat
Pada project kali ini saya memberikan tutorial tentang bagaimana cara menginstal django menggunakan python

## Kita memerlukan beberapa tools
1. saya menggunakan Vscode sebagai code editor
2. kita memerlukan python (minimal versi 3)
3. kita perlu juga Git dan browser chrome atau firefox
4. Virtualenv sebagai tool yang akan membuat lingkungan virtual yang terisolasi dan pip sebagai tool yang di pakai untuk menginstall django

# Note
## jika menginstall python biasanya Viartualenv dan pip otomatis terinstall

# Instalasi Django di Windows
1. buat folder .venv (disini saya memakai .venv)
2. masuk folder .venv dan buat virtualenv menggunakan perintah 
```
py -m venv .venv
```
3. aktifkan .venv dengan ketik 
```
cd .venv/Scripts
```
4. setelah masuk di dalam folder Scripts, ketik 
```
activate
```
5. jika .venv telah aktif, kita bisa melanjutkan menginstall django dengan mengetik
```
pip install django
```
6. untuk mengetahui library django terinstall, ketik 
```
pip list
```
7. selanjutnya kita akan membuat project django dengan mengetik 
```
"django-admin startproject mainwebsite"
``` 
(disini saya menggunakan mainwebsite)
8. untuk mengecek django terinstal, ketik 
```
py manage.py runserver
```