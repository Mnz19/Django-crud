from django.views.generic import ListView, CreateView, UpdateView, DeleteView , DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import AgendamentoExame , User, Exame
from .forms import AgendamentoExameForm, AdminAgendamentoExameForm, AdminExameForm
from django.urls import reverse_lazy
from django.db.models import Q, Count



class IndexView(ListView):
    template_name = 'index.html'
    model = AgendamentoExame
    context_object_name = 'agendamentos'
    
    def get_queryset(self):
        query = 0
        if self.request.user.is_authenticated:
            query = AgendamentoExame.objects.filter(usuario=self.request.user, ativo=True)
        return query

class DetailView(DetailView):
    template_name = 'detail.html'
    model = AgendamentoExame
    context_object_name = 'agendamentos'

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
    
    
class DeleteView(DeleteView):
    template_name = 'delete.html'
    model = AgendamentoExame
    context_object_name = 'agendamentos'
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
# A view administração

class AdminIndexView(UserPassesTestMixin, ListView):
    model = AgendamentoExame 
    template_name = 'adm/agendamento/list.html'
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
        context['qtd_agentamentos'] = self.get_queryset().count()
        return context


class AdminUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'adm/agendamento/update.html'
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
    
class AdminDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'adm/agendamento/delete.html'
    model = AgendamentoExame
    context_object_name = 'agendamentos'
    success_url = reverse_lazy('admin')
        
    def test_func(self):
        return self.request.user.is_superuser
    
class AdminUserView(UserPassesTestMixin, ListView):
    model = User
    template_name = 'adm/cliente/list.html'
    context_object_name = 'usuarios'
    
    def get_queryset(self):
        query = super().get_queryset().filter(is_superuser=False)
        filtro_usuario = self.request.GET.get('filtro_usuario')
        if filtro_usuario:
            query = query.filter(Q(username__startswith=filtro_usuario))
        
        query = query.annotate(qtd_agentamentos=Count('agendamentoexame'))
        return query.order_by('-qtd_agentamentos')
    
    def test_func(self):
        return self.request.user.is_superuser
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        usuarios = self.get_queryset().annotate(qtd_agentamentos=Count('agendamentoexame'))
        usuarios_com_agendamentos = usuarios.filter(qtd_agentamentos__gt=0)
        
        qtd_agentamentos_total = self.get_queryset().aggregate(qtd_agentamentos=Count('agendamentoexame'))
        
        context['qtd_agentamentos'] = qtd_agentamentos_total['qtd_agentamentos']
        context['qtd_usuarios'] = self.get_queryset().count()
        context['qtd_user_agentamentos'] = usuarios_com_agendamentos.count()
        return context

class AdminUserDetailView(UserPassesTestMixin, DetailView):
    model = User
    template_name = 'adm/cliente/detail.html'
    context_object_name = 'usuario'
    
    def test_func(self):
        return self.request.user.is_superuser
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filtro_andamento = self.request.GET.get('filtro_andamento')
        filtro_data = self.request.GET.get('filtro_data')
        usuario = self.get_object()
        agendamentos = usuario.agendamentoexame_set.all()
        if filtro_andamento:
            agendamentos = agendamentos.filter(andamento=filtro_andamento)
        if filtro_data:
            agendamentos = agendamentos.filter(data=filtro_data)
        context['agendamentos'] = agendamentos 
        return context

class AdminExameView(UserPassesTestMixin, ListView):
    model = Exame
    template_name = 'adm/exame/list.html'
    context_object_name = 'exames'
    
    def test_func(self):
        return self.request.user.is_superuser
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AdminExameCreateView(UserPassesTestMixin, CreateView):
    model = Exame
    template_name = 'adm/exame/create.html'
    form_class = AdminExameForm
    success_url = reverse_lazy('exames_admin')
    
    def test_func(self):
        return self.request.user.is_superuser
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)

class AdminExameDeleteView(UserPassesTestMixin, DeleteView):
    model = Exame
    template_name = 'adm/exame/delete.html'
    context_object_name = 'exame'
    success_url = reverse_lazy('exames_admin')
    
    def test_func(self):
        return self.request.user.is_superuser
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class AdminExameUpdateView(UserPassesTestMixin, UpdateView):
    model = Exame
    template_name = 'adm/exame/update.html'
    form_class = AdminExameForm
    context_object_name = 'exame'
    success_url = reverse_lazy('exames_admin')
    
    def test_func(self):
        return self.request.user.is_superuser
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context