from django.db import models
from django.core.validators import MaxValueValidator

class LevelRPG(models.Model):
    level = models.IntegerField(default=1, validators=[MaxValueValidator(20)])
    exp_needed = models.IntegerField(default=0)

    def __str__(self):
        return f"Level {self.level}"

    def is_max_level(self):
        return self.level >= 20

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