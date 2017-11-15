from rest_framework import serializers

from users.models import Admin

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admin
        fields = ('id', 'full_name', 'is_admin', 'email', 'username', 'password')