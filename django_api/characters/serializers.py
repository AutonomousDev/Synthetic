from rest_framework import serializers
from characters.models import (
    Character,
    Heritage,
    HeritageTrait,
    HeritageDrawback,
    ActiveSkillValue
)


class HeritageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heritage
        fields = ['name', 'description', 'free_traits', 'trait_with_drawback']


class HeritageTraitSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeritageTrait
        fields = ['name', 'description']


class ActiveSkillValueSerializer(serializers.ModelSerializer):
    skill = serializers.StringRelatedField()

    class Meta:
        model = ActiveSkillValue
        fields = ['skill', 'value']


class CharacterSerializer(serializers.ModelSerializer):
    heritage = HeritageSerializer(read_only=True)
    heritage_trait_1 = HeritageTraitSerializer(read_only=True)
    heritage_trait_2 = HeritageTraitSerializer(read_only=True)
    heritage_trait_3 = HeritageTraitSerializer(read_only=True)
    activeskillvalue_set = ActiveSkillValueSerializer(many=True, read_only=True)

    class Meta:
        model = Character
        fields = [
            'id',
            'name',
            'owner',
            'created',
            'strength',
            'body',
            'reaction',
            'intelligence',
            'willpower',
            'charisma',
            'zoetic_potential',
            'heritage',
            'uplifted_type',
            'heritage_trait_1',
            'heritage_trait_2',
            'heritage_trait_3',
            'heritage_drawback',
            'magic_ablity',
            'corporate_etiquette',
            'street_etiquette',
            'civic_etiquette',
            'aristocratic_etiquette',
            'military_etiquette',
            'criminal_etiquette',
            'wasteland_etiquette',
            'activeskillvalue_set'
        ]
