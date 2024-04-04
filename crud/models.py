from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):   
    criado = models.DateTimeField(verbose_name ='Criado em',auto_now_add=True)
    modificado = models.DateTimeField(verbose_name ='Modificado em',auto_now=True)
    ativo = models.BooleanField(verbose_name ='Ativo?',default=True)

    class Meta:
        abstract = True
        
class Exame(Base):
    nome = models.CharField('Nome',max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Exame'
        verbose_name_plural = 'Exames'
        ordering = ['nome']
        
class AgendamentoExame(Base):
    exame = models.ForeignKey(Exame,verbose_name='Exame',on_delete=models.CASCADE)
    data = models.DateField('Data',auto_now=False,auto_now_add=False)
    usuario = models.ForeignKey(User,verbose_name='Usuário',on_delete=models.CASCADE)
    HORARIO_CHOICES = (
    ('07:00', '07:00'),
    ('08:00', '08:00'),
    ('09:00', '09:00'),
    ('10:00', '10:00'),
    ('11:00', '11:00'),
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
    ('16:00', '16:00'),
    ('17:00', '17:00'),
)
    ANDAMENTO_CHOICES = (
        ('Agendado', 'Agendado'),
        ('Realizado', 'Realizado'),
        ('Enviado ao laboratório', 'Enviado ao laboratório'),
        ('Concluído', 'Concluído'),
        ('Cancelado', 'Cancelado'),
    )
    horario = models.CharField(verbose_name ='Horário', max_length = 5 ,choices=HORARIO_CHOICES)
    andamento = models.CharField(verbose_name ='Andamento',max_length=30,choices=ANDAMENTO_CHOICES,default='Agendado')
    resultado = models.FileField('Resultado',upload_to='pdfs/',null=True,blank=True)
    
    def __str__(self):
        data_formatada = self.data.strftime('%d/%m/%Y')
        return f"{self.usuario.username.capitalize()} - {self.exame.nome} - {data_formatada} - {self.horario}"

    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        ordering = ['data','horario']
        
        