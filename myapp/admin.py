from django.contrib import admin
from .models.character import CharacterRPG, ValorAtributo, CharacterHabilidade, CharacterItem
from .models.types import AtributoRPG, ClasseRPG, RaceRPG
from .models.values import EfeitoRPG, NaturezaRPG, LevelRPG
from .models.habilidades import Habilidade
from .models.itens import Item

# Register your models here.
class ValorAtributoInline(admin.TabularInline):
    model = ValorAtributo
    extra = 0

class HabilidadeInline(admin.TabularInline):
    model = CharacterHabilidade
    extra = 0

class ItemInline(admin.TabularInline):
    model = CharacterItem
    extra = 0

class CharacterRPGAdmin(admin.ModelAdmin):
    list_display = ('nome', 'classe', 'level', 'vivo', 'vida', 'mana')
    inlines = [ValorAtributoInline, HabilidadeInline, ItemInline]

admin.site.register(AtributoRPG)
admin.site.register(RaceRPG)
admin.site.register(ClasseRPG)
admin.site.register(CharacterRPG, CharacterRPGAdmin)
admin.site.register(EfeitoRPG)
admin.site.register(NaturezaRPG)
admin.site.register(Habilidade)
admin.site.register(Item)
admin.site.register(LevelRPG)