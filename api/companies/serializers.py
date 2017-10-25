from rest_framework import serializers

from companies.models import Company
from companies.models import Team


class CompanySerializer(serializers.ModelSerializer):
	pass

class TeamSerializer(serializers.ModelSerializer):

	class Meta:
        model = Team
        fields = '__all__'