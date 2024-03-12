from django.contrib import admin
from .models import Livro

class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'editora', 'lido')

admin.site.register(Livro, LivroAdmin)

