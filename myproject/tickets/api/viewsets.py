from rest_framework import viewsets
from tickets.api import serializers
from tickets import models

class EventoViewSet(viewsets.ModelViewSet):
    queryset = models.Evento.objects.all()
    serializer_class = serializers.EventoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = models.Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer

class IngressoViewSet(viewsets.ModelViewSet):
    queryset = models.Ingresso.objects.all()
    serializer_class = serializers.IngressoSerializer

class NotificacaoViewSet(viewsets.ModelViewSet):
    queryset = models.Notificacao.objects.all()
    serializer_class = serializers.NotificacaoSerializer
