from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import RecursoSerializador, ReservaSerializador, UsuarioSerializador
from .models import Recursos, Reservas
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializador
    
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
class RecursoViewSet(viewsets.ModelViewSet):
    queryset = Recursos.objects.all()
    serializer_class = RecursoSerializador
    
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reservas.objects.all()
    serializer_class = ReservaSerializador
    
    permission_classes=[IsAuthenticated]