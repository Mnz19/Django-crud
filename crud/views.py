from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView, UpdateView, DeleteView , DetailView
from .models import Livro
from .forms import LivroForm
from django.urls import reverse_lazy

class IndexView(ListView):
    template_name = 'index.html'
    model = Livro
    context_object_name = 'livros'
    
    def get_queryset(self):
        return Livro.objects.all().order_by('id')

class DetailView(DetailView):
    model = Livro
    template_name = 'detail.html'

class CreateView(CreateView):
    model = Livro
    form_class = LivroForm
    template_name = 'create.html'
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
class UpdateView(UpdateView):
    model = Livro
    form_class = LivroForm
    template_name = 'update.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    
class DeleteView(DeleteView):
    model = Livro
    template_name = 'delete.html'
    success_url = reverse_lazy('index')
    
    
   