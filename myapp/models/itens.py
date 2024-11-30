from django.db import models
from .values import EfeitoRPG, NaturezaRPG

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