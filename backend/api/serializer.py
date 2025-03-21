from django.contrib.auth.models import User
from rest_framework import serializers

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}} #dessa forma a senha só será aceita na hora de criar o User, não transportando a senha pelos requests

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) # aqui em '**validate_data' o django está separando os argumentos em dict e passando para a ORM para criar um novo user
        return User
    
    def __str__(self):
        return super().__str__()