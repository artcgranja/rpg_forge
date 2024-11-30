from django.db import models
from django.db.models import OneToOneField
from django.core.validators import MaxValueValidator

# Create your models here.
class AtributoRPG(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return self.nome

class ClasseRPG(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    main_atributo = models.ForeignKey(AtributoRPG, on_delete=models.CASCADE, related_name='atributo_principal')
    secundario_atributo = models.ForeignKey(AtributoRPG, on_delete=models.CASCADE, null=True, blank=True, related_name='atributo_secundario')
    mana = models.BooleanField(default=False)
    descricao = models.TextField(null=False, blank=False)
    def __str__(self):
        return self.nome

class RaceRPG(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    bonus_atributo = models.ForeignKey(AtributoRPG, on_delete=models.CASCADE, null=True, blank=True)
    bonus_valor = models.IntegerField(default=0)
    def __str__(self):
        return self.nome

class LevelRPG(models.Model):
    level = models.IntegerField(default=1, validators=[MaxValueValidator(20)])
    exp_needed = models.IntegerField(default=0)

    def __str__(self):
        return f"Level {self.level}"

    def is_max_level(self):
        return self.level >= 20

class CharacterRPG(models.Model):
    nome = models.CharField(max_length=100)
    race = models.ForeignKey(RaceRPG, on_delete=models.CASCADE, null=True, blank=True)
    classe = models.ForeignKey(ClasseRPG, on_delete=models.CASCADE)
    exp = models.IntegerField(default=0)
    level = models.ForeignKey(LevelRPG, on_delete=models.CASCADE, default=1)
    vivo = models.BooleanField(default=True)
    vida = models.IntegerField()
    mana = models.IntegerField(null=True, blank=True)
    descricao = models.TextField()
    atributos = models.ManyToManyField(AtributoRPG, through='ValorAtributo')

    def check_level_up(self):
        if self.exp >= self.level.exp_needed and not self.level.is_max_level():
            next_level = LevelRPG.objects.get(level=self.level.level + 1)
            self.exp -= self.level.exp_needed
            self.level = next_level
            self.save()
            return True
        return False

    def add_exp(self, amount):
        self.exp += amount
        self.save()
        return self.check_level_up()

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        
        if not self.classe.mana:
            self.mana = None

        if self.vida == 0 and self.vivo:
            self.death()

        if self.vivo == False and self.vida > 0:
            self.revive()

        leveled_up = self.check_level_up() if not is_new else False

        super().save(*args, **kwargs)

        if is_new:
            for atributo in AtributoRPG.objects.all():
                ValorAtributo.objects.create(
                    caracter=self,
                    atributo=atributo,
                    valor=0
                )

    def death(self):
        self.vivo = False
        self.save()
    
    def revive(self):
        self.vivo = True
        self.save()
    
    def __str__(self):
        return self.nome

class ValorAtributo(models.Model):
    caracter = models.ForeignKey(CharacterRPG, on_delete=models.CASCADE)
    atributo = models.ForeignKey(AtributoRPG, on_delete=models.CASCADE)
    valor = models.IntegerField(default=0)

    class Meta:
        unique_together = ['caracter', 'atributo']

    def __str__(self):
        return f"{self.caracter.nome} - {self.atributo.nome}: {self.valor}"
    
class EfeitoRPG(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    def __str__(self):
        return self.nome

class NaturezaRPG(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    def __str__(self):
        return self.nome

class Habilidade(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    efeito = models.ForeignKey(EfeitoRPG, on_delete=models.CASCADE)
    natureza = models.ForeignKey(NaturezaRPG, on_delete=models.CASCADE)
    valor = models.IntegerField(default=0, null=False, blank=False)
    acao_extra = models.BooleanField(default=False)
    descricao = models.TextField(null=False, blank=False)
    imagem = models.ImageField(upload_to='habilidades/', null=True, blank=True)
    def __str__(self):
        return self.nome

class Item(models.Model):
    nome = models.CharField(max_length=100)
    efeito = models.ForeignKey(EfeitoRPG, on_delete=models.CASCADE)
    natureza = models.ForeignKey(NaturezaRPG, on_delete=models.CASCADE)
    gasto_de_mana = models.IntegerField(default=0)
    valor = models.IntegerField(default=0)
    acao_extra = models.BooleanField(default=False)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='itens/', null=True, blank=True)
    def __str__(self):
        return self.nome
    
class CharacterHabilidade(models.Model):
    caracter = models.ForeignKey(CharacterRPG, on_delete=models.CASCADE)
    habilidade = models.ForeignKey(Habilidade, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.caracter.nome} - {self.habilidade.nome}"
    
class CharacterItem(models.Model):
    caracter = models.ForeignKey(CharacterRPG, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.caracter.nome} - {self.item.nome}"