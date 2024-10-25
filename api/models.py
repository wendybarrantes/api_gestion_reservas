from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    apellido_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    telefono_cliente = models.CharField( max_length=15)
    clave_cliente = models.CharField(max_length=15)
    
class Zonas_disponibles(models.Model):
    oficinas = models.BooleanField(default=True)  # True indica que está disponible
    salas_de_reuniones = models.BooleanField(default=True)
    escritorios = models.BooleanField(default=True)
    
def __str__(self):
    return (
        f"Oficinas: {'Disponibles' if self.oficinas else 'No Disponibles'}, "
        f"Salas de Reuniones: {'Disponibles' if self.salas_de_reuniones else 'No Disponibles'}, "
        f"Escritorios: {'Disponibles' if self.escritorios else 'No Disponibles'}"
    )

    
class Estado_reserva(models.Model):
     ESTADO_OPCIONES = [
        ('activa', 'Activa'),
        ('cancelada', 'Cancelada'),
        ('completada', 'Completada'),
        ('pendiente', 'Pendiente'),
        ('no_show', 'No Show'),
        ('expirada', 'Expirada'),
    ]
     estado = models.CharField(max_length=20, choices="ESTADO_OPCIONES", unique=True)

def __str__(self):
 return self.estado


class Reservar(models.Model):
    
    fecha_reserva = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    numero_personas = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    #llave foranea clientes
    cliente_FK = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    #llave foranea Zonas disponibles
    Zonas_disponibles_FK = models.ForeignKey(Zonas_disponibles, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"Reserva de {self.clientes} para {self.ZonasDisponibles} el {self.fecha_reserva}"
    
class Cancelar_reservas(models.Model):
    fecha_cancelacion = models.DateField()
    motivo = models.CharField(max_length=100)
    reserva_FK = models.models.ForeignKey(Reservar, on_delete=models.CASCADE)