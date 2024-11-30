from django.contrib import admin
from .models import (AtributoRPG, ClasseRPG, CharacterRPG, ValorAtributo, EfeitoRPG, 
                     NaturezaRPG, Habilidade, Item, CharacterHabilidade, CharacterItem, RaceRPG, LevelRPG)

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