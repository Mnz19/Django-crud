from django.urls import path
from .views import IndexView, CreateView, UpdateView, DeleteView , DetailView
from .views import AdminIndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', CreateView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', DetailView.as_view(), name='detail'),  
    #Administração
    path('adm/', AdminIndexView.as_view(), name='admin'), 
]

