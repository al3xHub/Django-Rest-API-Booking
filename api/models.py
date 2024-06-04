from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Recursos(models.Model):
    class Meta:
        verbose_name = "Recurso"
        
    RECURSO_TIPO=[
        ('HU', 'Humano'),
        ('FI', 'Financiero'),
        ('MA', 'Material'),
        ('TE', 'Técnico')]
    
    nombre = models.CharField(max_length=50)
    descripcion= models.TextField(max_length=255, null=True, blank=True)
    tipo = models.CharField(max_length=2, choices=RECURSO_TIPO, default='MA')
    
    def __str__(self):
        return f'{self.pk} - {self.nombre} : {self.descripcion}'
    
class Reservas(models.Model):
    class Meta:
        verbose_name = "Reserva"
        order_with_respect_to = 'user'
    
    RECURSO_TIPO=[
        ('SO', 'Solicitado'),
        ('CO', 'Concedido'),
        ('US', 'En uso'),
        ('FI', 'Finalizado')]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recurso = models.ForeignKey(Recursos, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    estado = models.CharField(max_length=2, choices=RECURSO_TIPO, default='SO')
    
    def __str__(self):
        return f'{self.pk} - {self.user} : {self.recurso}'
    
