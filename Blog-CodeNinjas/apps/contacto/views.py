from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Contacto
from .forms import ContactoForm, FormularioMensaje # Se agregó FormularioMensaje
from django.core.mail import send_mail

class ContactoCreateView(CreateView):
    model = Contacto
    form_class = ContactoForm
    template_name = 'contacto/contacto.html'
    success_url = reverse_lazy('index')

def enviar_mensaje(request):
    if request.method == 'POST':
        form = FormularioMensaje(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo_electronico']
            mensaje = form.cleaned_data['mensaje']
            
            send_mail(
                f'Mensaje de {nombre}',
                mensaje,
                correo,
                ['tu_correo_de_destino@example.com'],
            )
            return redirect('apps.contacto:mensaje_enviado')
    else:
        form = FormularioMensaje()
    
    return render(request, 'contacto/enviar_mensaje.html', {'form': form})