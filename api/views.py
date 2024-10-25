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
    
    
# Creacion de views de Zonas disponibles (metodos).
class Zonas_disponiblesListCreate(generics.ListCreateAPIView):  #POST
    queryset = Zonas_disponibles.objects.all()
    serializer_class = zonas_disponiblesSerializer
    
class Zonas_disponiblesDetail(generics.RetrieveUpdateDestroyAPIView): #GET
    queryset = Zonas_disponibles.objects.all()
    serializer_class = zonas_disponiblesSerializer
    
class Zonas_disponoblesUpdate(generics.UpdateAPIView): #UPDATE
    queryset = Zonas_disponibles.objects.all()
    serializer_class = zonas_disponiblesSerializer
    lookup_field = 'id'
    
class Zonas_disponoblesDelete(generics.UpdateAPIView): #DELETE
    queryset = Zonas_disponibles.objects.all()
    serializer_class = zonas_disponiblesSerializer
    lookup_field = 'id'
    
    
    # Creacion de views de Estado reserva (metodos).
class Estado_reservaListCreate(generics.ListCreateAPIView):  #POST
    queryset = Estado_reserva.objects.all()
    serializer_class = Estado_reservaSerializer
    
class Estado_reservaDetail(generics.RetrieveUpdateDestroyAPIView): #GET
    queryset = Estado_reserva.objects.all()
    serializer_class = Estado_reservaSerializer
    
class Estado_reservaUpdate(generics.UpdateAPIView): #UPDATE
    queryset = Estado_reserva.objects.all()
    serializer_class = Estado_reservaSerializer
    lookup_field = 'id'
    
class Estado_reservaDelete(generics.UpdateAPIView): #DELETE
    queryset = Estado_reserva.objects.all()
    serializer_class = Estado_reservaSerializer
    lookup_field = 'id'