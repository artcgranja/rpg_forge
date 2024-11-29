from django.shortcuts import render, HttpResponse
from .models import ClasseRPG, CharacterRPG, Habilidade

# Create your views here.
def index(request):
    habilidades = Habilidade.objects.all()
    return render(request, 'index.html', {'habilidades': habilidades})

def classes(request):
    classes = ClasseRPG.objects.all()
    return render(request, 'classes.html', {'classes': classes})

def caracters(request):
    caracters = CharacterRPG.objects.all()
    return render(request, 'caracters.html', {'caracters': caracters})

def habilidades(request):
    habilidades = Habilidade.objects.all()
    return render(request, 'habilidades.html', {'habilidades': habilidades})
