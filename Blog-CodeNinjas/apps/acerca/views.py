from django.shortcuts import render

def acerca_de(request):
    return render(request, 'acerca/acerca.html')
