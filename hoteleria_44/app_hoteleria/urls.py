from django.urls import path, re_path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    # Redirección de la raíz a la lista de clientes
    path('', views.index, name='index'),
    

    # Rutas para Cliente
    path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente_detail'),
    path('clientes/crear/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/<int:pk>/eliminar/', views.ClienteDeleteView.as_view(), name='cliente_delete'),

    # Rutas para Habitacion
    path('habitaciones/', views.HabitacionListView.as_view(), name='habitacion_list'),
    path('habitaciones/<int:pk>/', views.HabitacionDetailView.as_view(), name='habitacion_detail'),
    path('habitaciones/crear/', views.HabitacionCreateView.as_view(), name='habitacion_create'),
    path('habitaciones/<int:pk>/editar/', views.HabitacionUpdateView.as_view(), name='habitacion_update'),
    path('habitaciones/<int:pk>/eliminar/', views.HabitacionDeleteView.as_view(), name='habitacion_delete'),

    # Rutas para Empleado
    path('empleados/', views.EmpleadoListView.as_view(), name='empleado_list'),
    path('empleados/<int:pk>/', views.EmpleadoDetailView.as_view(), name='empleado_detail'),
    path('empleados/crear/', views.EmpleadoCreateView.as_view(), name='empleado_create'),
    path('empleados/<int:pk>/editar/', views.EmpleadoUpdateView.as_view(), name='empleado_update'),
    path('empleados/<int:pk>/eliminar/', views.EmpleadoDeleteView.as_view(), name='empleado_delete'),

    # Rutas para Reserva
    path('reservas/', views.ReservaListView.as_view(), name='reserva_list'),
    path('reservas/<int:pk>/', views.ReservaDetailView.as_view(), name='reserva_detail'),
    path('reservas/crear/', views.ReservaCreateView.as_view(), name='reserva_create'),
    path('reservas/<int:pk>/editar/', views.ReservaUpdateView.as_view(), name='reserva_update'),
    path('reservas/<int:pk>/eliminar/', views.ReservaDeleteView.as_view(), name='reserva_delete'),

    # Rutas para Pago
    path('pagos/', views.PagoListView.as_view(), name='pago_list'),
    path('pagos/<int:pk>/', views.PagoDetailView.as_view(), name='pago_detail'),
    path('pagos/crear/', views.PagoCreateView.as_view(), name='pago_create'),
    path('pagos/<int:pk>/editar/', views.PagoUpdateView.as_view(), name='pago_update'),
    path('pagos/<int:pk>/eliminar/', views.PagoDeleteView.as_view(), name='pago_delete'),
]
