from django import forms
from .models import AgendamentoExame, Exame
from django.core.exceptions import ValidationError
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User



class AgendamentoExameForm(forms.ModelForm):
    
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
            'data': forms.DateInput(format=('%d/%m/%Y'),attrs={'class':'form-floating','type':'date'}),
            'exame': forms.Select(attrs={'placeholder': 'Selecione seu exame' ,'class': 'form-floating'},),
            'horario': forms.Select(attrs={'class': 'form-floating'}),
        }
    
class AdminAgendamentoExameForm(forms.ModelForm):
    def clean(self):
        andamento = self.cleaned_data.get('andamento')
        
        if andamento == 'Concluído':
            resultado = self.cleaned_data.get('resultado')  
            if not resultado:
                raise ValidationError('Insira um arquivo de resultado')
        
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

class AdminExameForm(forms.ModelForm):
    class Meta:
        model = Exame
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-floating'}),
        }
        
class AdminUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'password' ,'is_staff','is_active']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-floating'}),
            'first_name': forms.TextInput(attrs={'class': 'form-floating'}),
            'last_name': forms.TextInput(attrs={'class': 'form-floating'}),
            'email': forms.EmailInput(attrs={'class': 'form-floating'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }