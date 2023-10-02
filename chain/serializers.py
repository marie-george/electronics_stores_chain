from rest_framework import serializers
from chain.models import ChainUnit
from chain.validators import hierarchy_level_validator


class ChainUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChainUnit
        fields = '__all__'
        # validators = [hierarchy_level_validator]
