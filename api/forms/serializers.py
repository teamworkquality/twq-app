from rest_framework import serializers

from forms.models import Form


class Form(serializers.ModelSerializer):

    class Meta:
        model = Form
        fields = ('id', 'name', 'is_admin', 'email')
        read_only_fields = ('full_name', 'is_admin', 'email')