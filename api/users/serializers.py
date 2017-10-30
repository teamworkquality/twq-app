from rest_framework import serializers

from users.models import User, Employee

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'full_name', 'is_admin', 'email')
        read_only_fields = ('full_name', 'is_admin', 'email')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'full_name', 'is_admin', 'email', 'team', 'company')
        read_only_fields = ('full_name', 'is_admin', 'email', 'team', 'company')