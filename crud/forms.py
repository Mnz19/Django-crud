from django import forms
from .models import AgendamentoExame
from django.core.exceptions import ValidationError
from datetime import datetime
from django.utils import timezone



class AgendamentoExameForm(forms.ModelForm):
    
    def clean(self):
        data = self.cleaned_data.get('data')
        horario = self.cleaned_data.get('horario')
        horario_time = datetime.strptime(horario, '%H:%M').time()

        if data < datetime.today().date():
            raise ValidationError('Data inválida, Insira uma data futura')
        
        if data == timezone.now().date() and horario_time <= timezone.now().time():
            raise ValidationError('Horário inválido, Insira um horário futuro')
        
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
