from django.db import models

class Base(models.Model):
    criado = models.DateField(auto_now_add=True)
    modificado = models.DateField(auto_now=True)
    lido = models.BooleanField(default=False)

    class Meta:
        abstract = True

class Livro(Base):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    sinopse = models.TextField()

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['titulo']
        