from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, View
from django.contrib.auth import login, authenticate
from .models import Usuario
from .forms import RegistroForm
from django.urls import reverse_lazy
from apps.posts.models import Post
from django.contrib.auth.models import Group

class AjaxLoginView(View):
    def post(self, request, *args, **kwargs):
        if request.headers.get("x-requested-with") != "XMLHttpRequest":
            return JsonResponse({"success": False, "error": "Solicitud inválida"})

        username = request.POST.get("username")
        password = request.POST.get("password")
        next_url = request.POST.get('next') or '/'

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return JsonResponse({"success": True, "redirect_url": next_url})
        else:
            return JsonResponse({"success": False, "error": "Credenciales incorrectas"})


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    # La línea `success_url` ya no es necesaria aquí si se configura en settings.py

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["error"] = 'Credenciales inválidas'
        context['ultimos_posts'] = Post.objects.all().order_by('-publicado')[:3]
        return context

    def post(self, request, *args, **kwargs):
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            self.request.POST = request.POST.copy()
            return super().post(request, *args, **kwargs)
        return super().post(request, *args, **kwargs)


class RegistroView(CreateView):
    model = Usuario
    template_name = 'registration/register.html'
    form_class = RegistroForm
    success_url = reverse_lazy('apps.usuario:login')

    def form_valid(self, form):
        response= super().form_valid(form)
        group=Group.objects.get(name='Registrado')
        self.object.groups.add(group)
        return redirect ('apps.usuario:registrar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimos_posts'] = Post.objects.all().order_by('-publicado')[:3]
        return context
        
def logout_page(request):
    return render(request, 'logout.html')

