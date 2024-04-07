from django.urls import path
from .views import UserIndexView, UserCreateView, UserUpdateView, UserDeleteView , UserDetailView
from .views import AdminIndexView, AdminUpdateView, AdminDeleteView, AdminUserView, AdminUserDetailView, AdminExameView, AdminExameCreateView, AdminExameDeleteView, AdminExameUpdateView, AdminUserCreateView, AdminUserUpdateView, AdminUserDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Usuário path
    
    path('', UserIndexView.as_view(), name='index'),
    path('agendar/', UserCreateView.as_view(), name='create'),
    path('editar/<int:pk>/', UserUpdateView.as_view(), name='update'),
    path('cancelar/<int:pk>/', UserDeleteView.as_view(), name='delete'),
    path('detalhes/<int:pk>/', UserDetailView.as_view(), name='detail'),  
    
    #Administração path
    
    path('agendamentos-admin/', AdminIndexView.as_view(), name='admin'), 
    path('agendamentos-admin/alterar-agendamento/<int:pk>/', AdminUpdateView.as_view(), name='update_admin'),
    path('agendamentos-admin/excluir-agendamento/<int:pk>/', AdminDeleteView.as_view(), name='delete_admin'),
    path('usuarios-admin/', AdminUserView.as_view(), name='usuarios_admin'),
    path('usuarios-admin/cadastrar-user/', AdminUserCreateView.as_view(), name='usuarios_create_admin'),
    path('usuarios-admin/detalhes/<int:pk>/', AdminUserDetailView.as_view(), name='usuarios_detail_admin'),
    path('usuarios-admin/editar/<int:pk>/', AdminUserUpdateView.as_view(), name='usuarios_update_admin'),
    path('usuarios-admin/delete/<int:pk>/', AdminUserDeleteView.as_view(), name='usuarios_delete_admin'),
    path('exames-admin/', AdminExameView.as_view(), name='exames_admin'),
    path('exames-admin/adicionar/', AdminExameCreateView.as_view(), name='exames_create_admin'),
    path('exames-admin/editar/<int:pk>/', AdminExameUpdateView.as_view(), name='exames_update_admin'),
    path('exames-admin/delete/<int:pk>/', AdminExameDeleteView.as_view(), name='exames_delete_admin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


