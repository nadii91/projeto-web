from django.db import models
from django.contrib.auth.models import User


TIPOS_USUARIO = (
    ('admin', 'Administrador'),
    ('organizador', 'Organizador'),
    ('visitante', 'Visitante'),
)


class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPOS_USUARIO, default='visitante')
    cidade = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} ({self.tipo})'


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Evento(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    data = models.DateField()
    local = models.CharField(max_length=150)
    cidade = models.CharField(max_length=100)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    imagem = models.ImageField(upload_to='eventos/', blank=True, null=True)
    faixa_etaria = models.CharField(max_length=50)
    organizador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='eventos')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Servico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    local = models.CharField(max_length=150)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Notificacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mensagem = models.TextField()
    cidade = models.CharField(max_length=100)
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notif. para {self.usuario.username} em {self.cidade}'
