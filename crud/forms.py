from django import forms
from .models import AgendamentoExame, Exame
from django.core.exceptions import ValidationError
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import ModelForm



class AgendamentoExameForm(ModelForm):
    
    def clean(self):
        data = self.cleaned_data.get('data')
        horario = self.cleaned_data.get('horario')
        horario_time = datetime.strptime(horario, '%H:%M').time()

        if data < datetime.today().date():
            raise ValidationError('Data inválida, Insira uma data válida')
        
        if data == timezone.now().date() and horario_time <= timezone.now().time():
            raise ValidationError('Horário inválido, Insira um horário válido')
    
        return self.cleaned_data
    
    class Meta:
        model = AgendamentoExame
        fields = ['exame','data','horario']
        widgets = {
            'data': forms.TextInput(attrs={'class': 'form-floating', 'type': 'date'}),
            'exame': forms.Select(attrs={'placeholder': 'Selecione seu exame' ,'class': 'form-floating'},),
            'horario': forms.Select(attrs={'class': 'form-floating'}),
        }

class AgendamentoExameUpdateForm(ModelForm):
    
    class Meta:
        model = AgendamentoExame
        fields = ['exame','data','horario']
        widgets = {
            'data': forms.TextInput(attrs={'class': 'form-floating', 'type': 'date'}),
            'exame': forms.Select(attrs={'placeholder': 'Selecione seu exame' ,'class': 'form-floating'},),
            'horario': forms.Select(attrs={'class': 'form-floating'}),
        }

    
class AdminAgendamentoExameForm(ModelForm):
    def clean(self):
        andamento = self.cleaned_data.get('andamento')
        
        if andamento == 'Concluído':
            resultado = self.cleaned_data.get('resultado')  
            if not resultado:
                raise ValidationError('Insira um arquivo de resultado')
        else:
            resultado = self.cleaned_data.get('resultado')  
            if resultado:
                raise ValidationError('Atualize o andamento para Concluído para inserir um resultado')
            
        
        return self.cleaned_data
    class Meta:
        model = AgendamentoExame
        fields = ['exame','data','horario','andamento','resultado']
        widgets = {
            'data': forms.TextInput(attrs={'class': 'form-floating', 'type': 'date'}),
            'exame': forms.Select(attrs={'class': 'form-floating'}),
            'horario': forms.Select(attrs={'class': 'form-floating'}),
            'andamento': forms.Select(attrs={'class': 'form-floating'}),
            'resultado': forms.ClearableFileInput(attrs={'class': 'form-floating'}),
        }

class AdminExameForm(ModelForm):
    class Meta:
        model = Exame
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-floating'}),
        }

class AdminUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email','password']
        widgets ={
            'first_name': forms.TextInput(attrs={'class': 'form-floating' }),
            'last_name': forms.TextInput(attrs={'class': 'form-floating' }),
            'username': forms.TextInput(attrs={'class': 'form-floating' }),
            'email': forms.EmailInput(attrs={'class': 'form-floating'}),
            'password': forms.PasswordInput(attrs={'class': 'form-floating'}),
        }
        
class AdminUserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email', 'is_active']
        widgets ={
            'first_name': forms.TextInput(attrs={'class': 'form-floating' }),
            'last_name': forms.TextInput(attrs={'class': 'form-floating' }),
            'username': forms.TextInput(attrs={'class': 'form-floating' }),
            'email': forms.EmailInput(attrs={'class': 'form-floating'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
