from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'unidade', 'nome_do_paciente', 'quarto', 'id_leito', 'telefone'
    ordering = '-id',
    # list_filter = 'last_name',
    search_fields = 'id', 'nome_do_paciente', 'unidade', 'quarto', 'id_leito'
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'nome_do_paciente',
    list_display_links = 'id', 'unidade',


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'nome',
    ordering = '-id',


@admin.register(models.Category2)
class Category2Admin(admin.ModelAdmin):
    list_display = 'nome',
    ordering = '-id',


@admin.register(models.Units)
class UnitsAdmin(admin.ModelAdmin):
    list_display = 'nome',
    ordering = '-id',
