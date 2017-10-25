from rest_framework import serializers

from .models import Company
from .models import Team


class CompanySerializer(serializers.ModelSerializer):
    pass

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'