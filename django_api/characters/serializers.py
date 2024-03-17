from rest_framework import serializers
from characters.models import (
    Character,
    Heritage,
    HeritageTrait,
    HeritageDrawback,
    UpliftedType,
    ActiveSkillValue,
    DeltaAttributes,
    DeltaBody
)


class DeltaAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeltaAttributes
        fields = [
            'strength',
            'strength_max',
            'body',
            'body_max',
            'reaction',
            'reaction_max',
            'intelligence',
            'intelligence_max',
            'willpower',
            'willpower_max',
            'charisma',
            'charisma_max'
        ]


class DeltaBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeltaBody
        fields = ['additional_arms', 'additional_legs']


class HeritageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heritage
        fields = ['name', 'description', 'free_traits', 'trait_with_drawback']


class HeritageTraitSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeritageTrait
        fields = ['name', 'description']


class UpliftedTypeSerializer(serializers.ModelSerializer):
    delta_attributes = DeltaAttributesSerializer(read_only=True)
    delta_body = DeltaBodySerializer(read_only=True)
    trait = HeritageTraitSerializer(read_only=True)

    class Meta:
        model = UpliftedType
        fields = [
            'name',
            'description',
            'attribute_cost',
            'small',
            'delta_attributes',
            'delta_body',
            'trait'
        ]


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
    uplifted_type = UpliftedTypeSerializer()

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
            # Active skill
            # Brawn Pool
            'melee_weapons',
            'unarmed_combat',
            'martial_arts',
            'throwing_weapons',
            'cybertechtronic_combat',
            'athletics',

            # Finesse Pool
            'firearms',
            'gunnery',
            'heavy_weapons',
            'energy_weapons',
            'archery',
            'articulated_maneuvers',

            # Focus Pool
            'shadow',
            'drive',
            'fly',
            'observation',
            'biotech',
            'reconnaissance',
            'locksmith',
            'computer_hacking',
            'computer_electronic_warfare',
            'computer_programming',
            'engineering_mechanical',
            'engineering_industrial',
            'engineering_aeronautics',
            'engineering_armory',
            'engineering_nautical',
            'artificing',
            'negotiations',

            # Resolve pool
            'rituals',
            'channeling',
            'sorcery',
            'astral_senses',
            'survival',
            'conjuring',
            'leadership',
            'subterfuge',
            'coercion',
            'fascination',

            # Etiquette
            'corporate_etiquette',
            'street_etiquette',
            'civic_etiquette',
            'aristocratic_etiquette',
            'military_etiquette',
            'criminal_etiquette',
            'wasteland_etiquette',

        ]
