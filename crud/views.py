from django.views.generic import ListView, CreateView, UpdateView, DeleteView , DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import AgendamentoExame
from .forms import AgendamentoExameForm
from django.urls import reverse_lazy

class IndexView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = AgendamentoExame
    context_object_name = 'agendamentos'
    
    def get_queryset(self):
        return AgendamentoExame.objects.filter(usuario=self.request.user, ativo=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = self.request.user.username.capitalize()
        context['is_admin'] = self.request.user.is_superuser
        return context

class DetailView(DetailView):
    template_name = 'detail.html'
    model = AgendamentoExame
    context_object_name = 'agendamentos'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = self.request.user.username.capitalize()
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
        context['usuario'] = self.request.user.username.capitalize()
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
        context['usuario'] = self.request.user.username.capitalize()
        context['is_admin'] = self.request.user.is_superuser
        return context
    
class DeleteView(DeleteView):
    template_name = 'delete.html'
    model = AgendamentoExame
    context_object_name = 'agendamentos'
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = self.request.user.username.capitalize()
        context['is_admin'] = self.request.user.is_superuser
        return context
    
    
   