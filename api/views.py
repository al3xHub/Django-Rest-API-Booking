from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import RecursoSerializador, ReservaSerializador, UsuarioSerializador
from .models import Recursos, Reservas

# Create your views here.
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializador
    
class RecursoViewSet(viewsets.ModelViewSet):
    queryset = Recursos.objects.all()
    serializer_class = RecursoSerializador
    
class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reservas.objects.all()
    serializer_class = ReservaSerializador