from django import forms
from .models import Livro
from django.core.exceptions import ValidationError

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'editora', 'sinopse' ,'lido']
    
    def limpar(self):
        limpar_dados = super().limpar()
        titulo = limpar_dados.get('titulo')
        autor = limpar_dados.get('autor')
        editora = limpar_dados.get('editora')
        sinopse = limpar_dados.get('sinopse')
        lido = limpar_dados.get('lido')

        if not (titulo and autor and editora and lido):
            raise ValidationError("Todos os campos devem ser preenchidos.")

        return limpar_dados
    
    
