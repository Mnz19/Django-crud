from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView, UpdateView, DeleteView , DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import AgendamentoExame , User, Exame
from .forms import AgendamentoExameForm, AdminAgendamentoExameForm, AdminExameForm, AdminUserForm, AdminUserUpdateForm
from django.urls import reverse_lazy
from django.db.models import Count


class UserIndexView(ListView):
    template_name = 'index.html'
    model = AgendamentoExame
    context_object_name = 'agendamentos'
    
    def get_queryset(self):
        query = ''
        filtro_exame = self.request.GET.get('filtro_exame')
        filtro_andamento = self.request.GET.get('filtro_andamento')
        filtro_data = self.request.GET.get('filtro_data')
        if self.request.user.is_authenticated:
            query = AgendamentoExame.objects.filter(usuario=self.request.user, ativo=True)
            if filtro_exame:
                query = query.filter(exame__nome__startswith=filtro_exame)
            if filtro_andamento:
                query = query.filter(andamento=filtro_andamento)
            if filtro_data:
                query = query.filter(data=filtro_data)
        return query

class UserDetailView(DetailView):
    template_name = 'detail.html'
    model = AgendamentoExame
    context_object_name = 'agendamentos'

class UserCreateView(CreateView):
    template_name = 'create.html'
    model = AgendamentoExame
    form_class = AgendamentoExameForm
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.save()
        return super().form_valid(form)
    
class UserUpdateView(UpdateView):
    model = AgendamentoExame
    form_class = AgendamentoExameForm
    template_name = 'update.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    
    
class UserDeleteView(DeleteView):
    template_name = 'delete.html'
    model = AgendamentoExame
    context_object_name = 'agendamentos'
    success_url = reverse_lazy('index')

    
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
        query = super().get_queryset().filter(is_superuser=False, is_active=True)
        filtro_usuario = self.request.GET.get('filtro_usuario')
        filtro_desativados = self.request.GET.get('filtro_desativados')
        filtro_adm = self.request.GET.get('filtro_adm')
        if filtro_usuario:
            query = query.filter(username__startswith=filtro_usuario)
        if filtro_desativados:
            query = super().get_queryset().filter(username__startswith=filtro_usuario ,is_active=False)
        if filtro_adm:
            query = super().get_queryset().filter(username__startswith=filtro_usuario ,is_superuser=True)

            
        query = query.annotate(qtd_agentamentos=Count('agendamentoexame'))
        return query.order_by('-qtd_agentamentos')
    
    def test_func(self):
        return self.request.user.is_superuser
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        usuarios = self.get_queryset()
        qtd_agentamentos_total = usuarios.aggregate(qtd_agentamentos=Count('agendamentoexame'))
        usuarios_com_agendamentos = usuarios.filter(qtd_agentamentos__gt=0)
        
        context['qtd_agentamentos'] = qtd_agentamentos_total['qtd_agentamentos']
        context['qtd_usuarios'] = usuarios.count()
        context['qtd_user_agentamentos'] = usuarios_com_agendamentos.count()
        return context

class AdminUserCreateView(UserPassesTestMixin, CreateView):
    model = User
    template_name = 'adm/cliente/create.html'
    form_class = AdminUserForm
    success_url = reverse_lazy('usuarios_admin')
    
    def test_func(self):
        return self.request.user.is_superuser
    
    def form_valid(self, form):
        user = form.save(commit=False) 
        user.set_password(form.cleaned_data['password'])
        user.save() 
        return super().form_valid(form)


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
        context['usuario_nome'] = usuario.username.capitalize()
        context['agendamentos'] = agendamentos 
        context['user'] = self.request.user
        return context
    
class AdminUserUpdateView(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'adm/cliente/update.html'
    form_class = AdminUserUpdateForm
    context_object_name = 'usuario'
    success_url = reverse_lazy('usuarios_admin')
    
    def test_func(self):
        return self.request.user.is_superuser
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class AdminUserDeleteView(UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'adm/cliente/delete.html'
    context_object_name = 'usuario'
    success_url = reverse_lazy('usuarios_admin')
    
    def test_func(self):
        return self.request.user.is_superuser

class AdminExameView(UserPassesTestMixin, ListView):
    model = Exame
    template_name = 'adm/exame/list.html'
    context_object_name = 'exames'
    
    def get_queryset(self):
        query = super().get_queryset()
        filtro_nome = self.request.GET.get('filtro_nome')
        if filtro_nome:
            query = query.filter(nome__startswith=filtro_nome)
        return query
    
    def test_func(self):
        return self.request.user.is_superuser

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

class AdminExameDeleteView(UserPassesTestMixin, DeleteView):
    model = Exame
    template_name = 'adm/exame/delete.html'
    context_object_name = 'exame'
    success_url = reverse_lazy('exames_admin')
    
    def test_func(self):
        return self.request.user.is_superuser

    
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
    