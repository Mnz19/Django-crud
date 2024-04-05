from django.views.generic import ListView, CreateView, UpdateView, DeleteView , DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import AgendamentoExame
from .forms import AgendamentoExameForm, AdminAgendamentoExameForm
from django.urls import reverse_lazy
from django.shortcuts import render




class IndexView(ListView):
    template_name = 'index.html'
    model = AgendamentoExame
    context_object_name = 'agendamentos'
    
    def get_queryset(self):
        query = 0
        if self.request.user.is_authenticated:
            query = AgendamentoExame.objects.filter(usuario=self.request.user, ativo=True)
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_admin'] = self.request.user.is_superuser
        return context

class DetailView(DetailView):
    template_name = 'detail.html'
    model = AgendamentoExame
    context_object_name = 'agendamentos'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_admin'] = self.request.user.is_superuser
        return context

class CreateView(CreateView):
    template_name = 'create.html'
    model = AgendamentoExame
    form_class = AgendamentoExameForm
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_admin'] = self.request.user.is_superuser
        return context
    
class UpdateView(UpdateView):
    model = AgendamentoExame
    form_class = AgendamentoExameForm
    template_name = 'update.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_admin'] = self.request.user.is_superuser
        return context
    
class DeleteView(DeleteView):
    template_name = 'delete.html'
    model = AgendamentoExame
    context_object_name = 'agendamentos'
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_admin'] = self.request.user.is_superuser
        return context
    
# A view administração

class AdminIndexView(UserPassesTestMixin, ListView):
    model = AgendamentoExame 
    template_name = 'adm/admin_index.html'
    context_object_name = 'agendamentos'
    def test_func(self):
        return self.request.user.is_superuser
    
    def get_queryset(self):
        queryset = super().get_queryset()
        filtro_andamento = self.request.GET.get('filtro_andamento')
        filtro_data = self.request.GET.get('filtro_data')
        if filtro_andamento:
            queryset = queryset.filter(andamento=filtro_andamento)
        if filtro_data:
            queryset = queryset.filter(data=filtro_data)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_admin'] = self.request.user.is_superuser
        return context

class AdminUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'adm/admin_update.html'
    model = AgendamentoExame
    form_class = AdminAgendamentoExameForm
    context_object_name = 'agendamentos'
    success_url = reverse_lazy('admin')
    
    def test_func(self):
        return self.request.user.is_superuser
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_admin'] = self.request.user.is_superuser
        return context
    
class AdminDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'adm/admin_delete.html'
    model = AgendamentoExame
    context_object_name = 'agendamentos'
    success_url = reverse_lazy('admin')
        
    def test_func(self):
        return self.request.user.is_superuser
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_admin'] = self.request.user.is_superuser
        return context