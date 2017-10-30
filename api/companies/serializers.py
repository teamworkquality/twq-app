from rest_framework import serializers

from .models import Company, Team, Employee


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'full_name', 'is_admin', 'email', 'team', 'company')
        read_only_fields = ('full_name', 'is_admin', 'email', 'team', 'company')