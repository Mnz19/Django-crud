from django import forms
from .models import AgendamentoExame
from django.core.exceptions import ValidationError
import datetime

class AgendamentoExameForm(forms.ModelForm):
    
    def clean(self):
        data = self.cleaned_data.get('data')
        if data < datetime.date.today():
            raise ValidationError('Data inválida, Insira uma data futura')
        return self.cleaned_data
    
    class Meta:
        model = AgendamentoExame
        fields = ['exame','data','horario']
        widgets = {
            'data': forms.DateInput(format=('%d/%m/%Y'),attrs={'class':'form-floating','placeholder':'Select a date','type':'date'}),
            
        }
    
    
