from django.contrib import admin
from .models import Cliente, Habitacion, Empleado, Reserva, Pago

admin.site.register(Cliente)
admin.site.register(Habitacion)
admin.site.register(Empleado)
admin.site.register(Reserva)
admin.site.register(Pago)
