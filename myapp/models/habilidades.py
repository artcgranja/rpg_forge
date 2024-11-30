from django.db import models
from .values import EfeitoRPG, NaturezaRPG

class Habilidade(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    efeito = models.ForeignKey(EfeitoRPG, on_delete=models.CASCADE)
    natureza = models.ForeignKey(NaturezaRPG, on_delete=models.CASCADE)
    valor = models.IntegerField(default=0, null=False, blank=False)
    acao = models.IntegerField(default=0)
    acao_extra = models.IntegerField(default=0)
    mana_gasto = models.IntegerField(default=0)
    descricao = models.TextField(null=False, blank=False)
    imagem = models.ImageField(upload_to='habilidades/', null=True, blank=True)
    def __str__(self):
        return self.nome