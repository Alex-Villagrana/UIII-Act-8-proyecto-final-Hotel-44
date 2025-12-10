from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} ({self.email})"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Habitacion(models.Model):
    ESTADOS = [
        ('DISPONIBLE', 'Disponible'),
        ('OCUPADA', 'Ocupada'),
        ('MANTENIMIENTO', 'Mantenimiento'),
    ]

    id_habitacion = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=50)
    precio_noche = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='DISPONIBLE')

    def __str__(self):
        return f"Habitación {self.numero} - {self.tipo}"

    class Meta:
        verbose_name = "Habitación"
        verbose_name_plural = "Habitaciones"


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    turno = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - {self.cargo}"


class Reserva(models.Model):
    ESTADOS_RESERVA = [
        ('PENDIENTE', 'Pendiente'),
        ('CONFIRMADA', 'Confirmada'),
        ('CANCELADA', 'Cancelada'),
    ]
    id_reserva = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='id_cliente')
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, db_column='id_habitacion')
    
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADOS_RESERVA, default='PENDIENTE')

    def __str__(self):
        return f"Reserva #{self.id_reserva} - {self.cliente.nombre}"


class Pago(models.Model):
    ESTADOS_PAGO = [
        ('PENDIENTE', 'Pendiente'),
        ('PAGADO', 'Pagado'),
        ('REEMBOLSADO', 'Reembolsado'),
    ]

    id_pago = models.AutoField(primary_key=True)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, db_column='id_reserva')
    
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    fecha_pago = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS_PAGO, default='PENDIENTE')

    def __str__(self):
        return f"Pago #{self.id_pago} - {self.monto}"
