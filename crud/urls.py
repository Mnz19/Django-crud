from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('index', class_view.index, name='index'),
]
