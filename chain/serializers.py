from rest_framework import serializers
from chain.models import ChainUnit
from chain.validators import hierarchy_level_validator


class ChainUnitSerializer(serializers.ModelSerializer):
    """Стандартный сериализатор, используется для большинства эндпойнтов"""
    class Meta:
        model = ChainUnit
        fields = '__all__'
        validators = [hierarchy_level_validator]


class ChainUnitUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для эдпойнта Update - не позволяет изменять поле Задолженность"""
    class Meta:
        model = ChainUnit
        fields = '__all__'
        validators = [hierarchy_level_validator]
        read_only_fields = ["debt"]
