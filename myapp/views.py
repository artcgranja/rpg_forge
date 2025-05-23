from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models.types import ClasseRPG, RaceRPG
from .models.character import CharacterRPG
from .models.habilidades import Habilidade
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if not remember_me:
                request.session.set_expiry(0)
            return redirect('myapp:index')
    
    return render(request, 'myapp/index/index.html')

def classes(request):
    classes = ClasseRPG.objects.all()
    return render(request, 'myapp/classes/classes.html', {'classes': classes})

def habilidades(request):
    habilidades = Habilidade.objects.all()
    return render(request, 'myapp/abilities/abilities.html', {'habilidades': habilidades})

def races(request):
    races = RaceRPG.objects.all()
    return render(request, 'myapp/races/races.html', {'races': races})

@login_required
def characters(request):
    characters = CharacterRPG.objects.filter(user=request.user)
    return render(request, 'myapp/characters/characters.html', {'characters': characters})

@login_required
def profile(request):
    return render(request, 'myapp/profile/profile.html')

def register(request):
    return render(request, 'myapp/register.html')

@login_required
def create_character(request):
    context = {
        'races': RaceRPG.objects.all(),
        'classes': ClasseRPG.objects.all(),
        'selected_race': None,
        'selected_classe': None,
        'selected_classe_info': None,
    }

    if request.method == 'POST':
        nome = request.POST.get('nome')
        race_id = request.POST.get('race')
        classe_id = request.POST.get('classe')
        descricao = request.POST.get('descricao')

        errors = {}
        if not nome:
            errors['nome'] = 'O nome é obrigatório.'
        if not race_id:
            errors['race'] = 'A raça é obrigatória.'
        if not classe_id:
            errors['classe'] = 'A classe é obrigatória.'
        if not descricao:
            errors['descricao'] = 'A descrição é obrigatória.'

        if errors:
            context.update({
                'form': {'errors': errors},
                'selected_race': race_id,
                'selected_classe': classe_id
            })
            messages.error(request, 'Por favor, corrija os erros no formulário.')
            return render(request, 'myapp/characters/create_character.html', context)

        try:
            race = RaceRPG.objects.get(id=race_id)
            classe = ClasseRPG.objects.get(id=classe_id)

            character = CharacterRPG(
                user=request.user,
                nome=nome,
                race=race,
                classe=classe,
                descricao=descricao
            )
            character.save()

            messages.success(request, f'Personagem {nome} criado com sucesso!')
            return redirect('myapp:characters')

        except (RaceRPG.DoesNotExist, ClasseRPG.DoesNotExist):
            messages.error(request, 'Raça ou Classe inválida.')
            return render(request, 'myapp/characters/create_character.html', context)
        
        except Exception as e:
            messages.error(request, f'Erro ao criar personagem: {str(e)}')
            return render(request, 'myapp/characters/create_character.html', context)

    return render(request, 'myapp/characters/create_character.html', context)

def get_classe_info(request, classe_id):
    print("Classe ID:", classe_id)
    try:
        classe = ClasseRPG.objects.get(id=classe_id)
        data = {
            'vida_base': classe.vida_base,
            'mana_base': classe.mana_base,
        }
        return JsonResponse(data)
    except ClasseRPG.DoesNotExist:
        return JsonResponse({'error': 'Classe não encontrada'}, status=404)
    
@login_required
def delete_character(request, character_id):
    print("User:", request.user)
    try:
        character = CharacterRPG.objects.get(id=character_id, user=request.user)
        print("Character encontrado:", character)
        character.delete()
        return JsonResponse({'status': 'success'})
    except CharacterRPG.DoesNotExist:
        print("Character não encontrado")
        return JsonResponse({'status': 'error', 'message': 'Character não encontrado'}, status=404)
    except Exception as e:
        print("Erro:", str(e))
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)