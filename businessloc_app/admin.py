from django.contrib import admin
from .models import *

# Register your models here.
from django.contrib.admin import ModelAdmin, TabularInline, ModelAdmin

class SubKriteriaInline(TabularInline):
    model = SubKriteria
    extra = 1

class KriteriaAdmin(ModelAdmin):
    inlines = [
        SubKriteriaInline,
    ]

admin.site.register(Alternatif)
admin.site.register(Kriteria, KriteriaAdmin)
admin.site.register(SubKriteria)
admin.site.register(Penilaian)