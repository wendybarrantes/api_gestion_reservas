from rest_framework import serializers
from models import Clientes
from models import Zonas_disponibles
from models import Estado_reserva
from models import Reservar
from models import Cancelar_reservas

class clientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fiels ='__all__'
        
class zonas_disponiblesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zonas_disponibles
        fiels = '__all__'    
        
class Estado_reservaSerializer(serializers.ModelSerializer):
    class meta:
        model = Estado_reserva
        fiels = '__all__'     
        
class ReservaSerializer(serializers.ModelSerializer):
    class meta:
        model= Reservar        
        fiels = '__all__'
        
class Cancelar_reservasSerializer(serializers.ModelSerializer):
    class meta:
        model = Cancelar_reservas
        fiels = '__all__'      
        
              