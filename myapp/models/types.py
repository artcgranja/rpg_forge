from django.db import models

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
    vida_base = models.IntegerField(default=0)
    mana_base = models.IntegerField(default=0)
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