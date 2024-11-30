from django.db import models
from .types import RaceRPG, ClasseRPG, AtributoRPG
from .values import LevelRPG
from .habilidades import Habilidade
from .itens import Item
from django.contrib.auth.models import User

class CharacterRPG(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    race = models.ForeignKey(RaceRPG, on_delete=models.CASCADE, null=True, blank=True)
    classe = models.ForeignKey(ClasseRPG, on_delete=models.CASCADE)
    exp = models.IntegerField(default=0)
    level = models.ForeignKey(LevelRPG, on_delete=models.CASCADE, default=1)
    vivo = models.BooleanField(default=True)
    vida = models.IntegerField(default=0)
    mana = models.IntegerField(null=True, blank=True, default=0)
    mana_max = models.IntegerField(default=0)
    vida_max = models.IntegerField(default=0)
    descricao = models.TextField()
    atributos = models.ManyToManyField(AtributoRPG, through='ValorAtributo')

    def check_level_up(self):
        if self.exp >= self.level.exp_needed and not self.level.is_max_level():
            next_level = LevelRPG.objects.get(level=self.level.level + 1)
            self.exp -= self.level.exp_needed
            self.level = next_level
            self.add_status_points(1)
            self.save()
            return True
        return False

    def add_exp(self, amount):
        self.exp += amount
        self.save()
        return self.check_level_up()

    def descansar(self):
        self.vida = self.vida_max
        self.mana = self.mana_max
        self.save()

    def add_status_points(self, amount):
        self.status_points.pontos += amount
        self.save()

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        
        if not self.classe.mana:
            self.mana = None

        if self.vida == 0 and self.vivo:
            self.death()

        if self.vivo == False and self.vida > 0:
            self.revive()

        super().save(*args, **kwargs)

        if is_new:
            self.vida_max = self.classe.vida_base
            self.mana_max = self.classe.mana_base
            self.vida = self.vida_max
            self.mana = self.mana_max

            existing_atributos = ValorAtributo.objects.filter(caracter=self).values_list('atributo_id', flat=True)
            
            for atributo in AtributoRPG.objects.all():
                if atributo.id not in existing_atributos:
                    valor = 8 + self.race.bonus_valor if atributo.nome == self.race.bonus_atributo.nome else 8
                    ValorAtributo.objects.create(
                        caracter=self,
                        atributo=atributo,
                        valor=valor
                    )

    def death(self):
        self.vivo = False
        self.save()
    
    def revive(self):
        self.vivo = True
        self.save()
    
    def __str__(self):
        return self.nome

class StatusPoints(models.Model):
    caracter = models.ForeignKey(CharacterRPG, on_delete=models.CASCADE)
    pontos = models.IntegerField(default=27)
    
    def __str__(self):
        return f"{self.caracter.nome} - Pontos: {self.pontos}"

class ValorAtributo(models.Model):
    caracter = models.ForeignKey(CharacterRPG, on_delete=models.CASCADE)
    atributo = models.ForeignKey(AtributoRPG, on_delete=models.CASCADE)
    valor = models.IntegerField(default=0)

    class Meta:
        unique_together = ['caracter', 'atributo']

    def __str__(self):
        return f"{self.caracter.nome} - {self.atributo.nome}: {self.valor}"

class CharacterItem(models.Model):
    caracter = models.ForeignKey(CharacterRPG, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.caracter.nome} - {self.item.nome}"
    
class CharacterHabilidade(models.Model):
    caracter = models.ForeignKey(CharacterRPG, on_delete=models.CASCADE)
    habilidade = models.ForeignKey(Habilidade, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.caracter.nome} - {self.habilidade.nome}"