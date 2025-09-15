from django.db import models

# Create your models here.


class Evento(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateTimeField()
    local = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome
    
class Ingresso(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    data_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ingresso para {self.evento.nome} comprado por {self.cliente.nome}"

class Notificacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notificação para {self.cliente.nome} enviada em {self.data_envio}"