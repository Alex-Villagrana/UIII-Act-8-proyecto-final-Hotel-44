from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cliente, Habitacion, Empleado, Reserva, Pago
from .forms import ReservaForm

def index(request):
    return render(request, 'index.html')

# Vistas para Cliente
class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente/cliente_detail.html'

class ClienteCreateView(CreateView):
    model = Cliente
    fields = '__all__'
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = '__all__'
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')

# Vistas para Habitacion
class HabitacionListView(ListView):
    model = Habitacion
    template_name = 'habitacion/habitacion_list.html'

class HabitacionDetailView(DetailView):
    model = Habitacion
    template_name = 'habitacion/habitacion_detail.html'

class HabitacionCreateView(CreateView):
    model = Habitacion
    fields = '__all__'
    template_name = 'habitacion/habitacion_form.html'
    success_url = reverse_lazy('habitacion_list')

class HabitacionUpdateView(UpdateView):
    model = Habitacion
    fields = '__all__'
    template_name = 'habitacion/habitacion_form.html'
    success_url = reverse_lazy('habitacion_list')

class HabitacionDeleteView(DeleteView):
    model = Habitacion
    template_name = 'habitacion/habitacion_confirm_delete.html'
    success_url = reverse_lazy('habitacion_list')

# Vistas para Empleado
class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'empleado/empleado_list.html'

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado/empleado_detail.html'

class EmpleadoCreateView(CreateView):
    model = Empleado
    fields = '__all__'
    template_name = 'empleado/empleado_form.html'
    success_url = reverse_lazy('empleado_list')

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    fields = '__all__'
    template_name = 'empleado/empleado_form.html'
    success_url = reverse_lazy('empleado_list')

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleado/empleado_confirm_delete.html'
    success_url = reverse_lazy('empleado_list')

# Vistas para Reserva
class ReservaListView(ListView):
    model = Reserva
    template_name = 'reserva/reserva_list.html'

class ReservaDetailView(DetailView):
    model = Reserva
    template_name = 'reserva/reserva_detail.html'

class ReservaCreateView(CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'reserva/reserva_form.html'
    success_url = reverse_lazy('reserva_list')

class ReservaUpdateView(UpdateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'reserva/reserva_form.html'
    success_url = reverse_lazy('reserva_list')

class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = 'reserva/reserva_confirm_delete.html'
    success_url = reverse_lazy('reserva_list')

# Vistas para Pago
class PagoListView(ListView):
    model = Pago
    template_name = 'pago/pago_list.html'

class PagoDetailView(DetailView):
    model = Pago
    template_name = 'pago/pago_detail.html'

class PagoCreateView(CreateView):
    model = Pago
    fields = '__all__'
    template_name = 'pago/pago_form.html'
    success_url = reverse_lazy('pago_list')

class PagoUpdateView(UpdateView):
    model = Pago
    fields = '__all__'
    template_name = 'pago/pago_form.html'
    success_url = reverse_lazy('pago_list')

class PagoDeleteView(DeleteView):
    model = Pago
    template_name = 'pago/pago_confirm_delete.html'
    success_url = reverse_lazy('pago_list')
