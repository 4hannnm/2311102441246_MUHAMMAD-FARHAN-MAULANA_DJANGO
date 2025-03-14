from django.contrib import admin
from pengguna.models import Biodata

# Register your models here.
class BiodataAdmin(admin.ModelAdmin):
    list_display = ['User','alamat','telpon']
    search_fields = ['User__username']
admin.site.register(Biodata, BiodataAdmin)