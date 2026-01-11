from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    descricao = models.TextField(blank=True)
    validade = models.DateField(null=True, blank=True)
    banca = models.CharField(max_length=100)  
    imagem_url = models.URLField(blank=True)  

    def __str__(self):
        return self.nome
