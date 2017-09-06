from rest_framework import serializers
from proyecto1.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields('id','usuario', 'password')
