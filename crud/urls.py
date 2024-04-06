from django.urls import path
from .views import IndexView, CreateView, UpdateView, DeleteView , DetailView
from .views import AdminIndexView, AdminUpdateView, AdminDeleteView, AdminUserView, AdminUserDetailView, AdminExameView, AdminExameCreateView, AdminExameDeleteView, AdminExameUpdateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', CreateView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', DetailView.as_view(), name='detail'),  
    #Administração
    path('adm/', AdminIndexView.as_view(), name='admin'), 
    path('alterar/<int:pk>/', AdminUpdateView.as_view(), name='update_admin'),
    path('excluir/<int:pk>/', AdminDeleteView.as_view(), name='delete_admin'),
    path('usuarios-admin/', AdminUserView.as_view(), name='usuarios_admin'),
    path('usuarios/<int:pk>/', AdminUserDetailView.as_view(), name='usuario_detail_admin'),
    path('exames-admin/', AdminExameView.as_view(), name='exames_admin'),
    path('exames-admin/create/', AdminExameCreateView.as_view(), name='exames_create_admin'),
    path('exames-admin/update/<int:pk>/', AdminExameUpdateView.as_view(), name='exames_update_admin'),
    path('exames-admin/delete/<int:pk>/', AdminExameDeleteView.as_view(), name='exames_delete_admin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


