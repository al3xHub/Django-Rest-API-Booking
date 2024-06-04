from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Recursos, Reservas

class RecursoSerializador(serializers.ModelSerializer):
    class Meta:
        model = Recursos
        fields = '__all__'
        #exclude = ('id',)
        
class ReservaSerializador(serializers.ModelSerializer):
    class Meta:
        model = Reservas
        fields = '__all__'
        
class UsuarioSerializador(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['url', 'id', 'username', 'email', 'is_staff']