from rest_framework import serializers
from tickets import models

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Evento
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = '__all__'

class IngressoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingresso
        fields = '__all__'

class NotificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notificacao
        fields = '__all__'