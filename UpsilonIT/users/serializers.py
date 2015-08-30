from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'first_name', 'last_name', 'email', 'created_at')
        write_only_fields = ('password', )
        read_only_fields = ('created_at', )