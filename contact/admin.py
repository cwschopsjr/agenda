from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'data_da_consulta', 'nome_do_paciente', 'cpf', 'telefone', 'show'
    ordering = '-id',
    # list_filter = 'last_name',
    search_fields = 'id', 'data_da_consulta', 'nome_do_paciente', 'cpf', 'hd'
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'show',
    list_display_links = 'id',


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'nome',
    ordering = '-id',


# @admin.register(models.Category2)
# class Category2Admin(admin.ModelAdmin):
#     list_display = 'nome',
#     ordering = '-id',


# @admin.register(models.Units)
# class UnitsAdmin(admin.ModelAdmin):
#     list_display = 'nome',
#     ordering = '-id',
