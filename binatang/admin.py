from django.contrib import admin
from .models import Hewan


@admin.register(Hewan)
class HewanAdmin(admin.ModelAdmin):
    list_display=('id','nama','species')
    ordering=('id',)
    search_fields=('nama',)