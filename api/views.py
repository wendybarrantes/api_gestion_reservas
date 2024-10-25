from django.shortcuts import render
from rest_framework import generics
from .models import Clientes, Zonas_disponibles,Estado_reserva,Reservar,Cancelar_reservas
from.serializers import clientesSerializer, zonas_disponiblesSerializer,Estado_reservaSerializer,ReservarSerializer,Cancelar_reservasSerializer

# Create your views here.

# Creacion de views de Clientes(metodos).
class ClientesListCreate(generics.ListCreateAPIView):  #POST
    queryset = Clientes.objects.all()
    serializer_class = clientesSerializer
    
class ClientesDetail(generics.RetrieveUpdateDestroyAPIView): #GET
    queryset = Clientes.objects.all()
    serializer_class = clientesSerializer
    
class ClientesUpdate(generics.UpdateAPIView): #UPDATE
    queryset = Clientes.objects.all()
    serializer_class = clientesSerializer
    lookup_field = 'id'
    
class ClientesDelete(generics.UpdateAPIView): #DELETE
    queryset = Clientes.objects.all()
    serializer_class = clientesSerializer
    lookup_field = 'id'
    
    # Creacion de views de Clientes(metodos).