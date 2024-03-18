from django.db import models
from django.contrib.auth.models import User
from characters.constants import DICE_POOL_CHOICES, MOVEMENT_TYPE_CHOICES
from django.contrib import admin


class ActiveSkillGroup(models.Model):
    group_name = models.CharField(max_length=100)

    def __str__(self):
        return self.group_name


class ActiveSkill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    skill_group = models.ForeignKey(ActiveSkillGroup, on_delete=models.PROTECT, blank=True, null=True)
    dice_pool = models.CharField(max_length=100, choices=DICE_POOL_CHOICES)

    def __str__(self):
        return self.name


class DeltaSkill(models.Model):
    skill = models.ForeignKey(ActiveSkill, on_delete=models.PROTECT)
    bonus_dice = models.IntegerField(default=0)
    modifier_dice = models.IntegerField(default=0)
    limit = models.IntegerField(default=0)

    def __str__(self):
        skill_value = ""
        skill_limit = ""

        if self.modifier_dice > 0:
            skill_value = self.skill.name + ": +" + str(self.modifier_dice)
        else:
            skill_value = self.skill.name + ": " + str(self.modifier_dice)

        if self.limit > 0:
            skill_limit = " Limit: +" + str(self.limit)
        else:
            skill_limit = ", Limit: " + str(self.limit)

        return skill_value + skill_limit


class DeltaBody(models.Model):
    # Body
    additional_arms = models.IntegerField(default=0)
    additional_legs = models.IntegerField(default=0)

    def has_related_object(self):
        return hasattr(self, 'related_object')

    def __str__(self):
        if hasattr(self, 'UpliftedType'):
            return self.UpliftedType.name + ": DeltaBody"
        elif hasattr(self, 'HeritageTrait'):
            return self.HeritageTrait.name + ": DeltaBody"
        else:
            return "Unassigned DeltaBody"


class DeltaAttributes(models.Model):
    # Attribute
    strength = models.IntegerField(default=0)
    strength_max = models.IntegerField(default=0)
    body = models.IntegerField(default=0)
    body_max = models.IntegerField(default=0)
    reaction = models.IntegerField(default=0)
    reaction_max = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    intelligence_max = models.IntegerField(default=0)
    willpower = models.IntegerField(default=0)
    willpower_max = models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)
    charisma_max = models.IntegerField(default=0)
    melee_reach = models.IntegerField(default=0)
    movement_distance = models.IntegerField(default=0)

    def __str__(self):
        if hasattr(self, 'UpliftedType'):
            return 'Uplifted type: ' + self.UpliftedType.name + " - DeltaAttributes"
        elif hasattr(self, 'HeritageTrait'):
            return 'Heritage Trait: ' + self.HeritageTrait.name + " - DeltaAttributes"
        else:
            return "Unassigned DeltaAttributes"


class DeltaDefence(models.Model):
    soak_test_bonus_dice = models.IntegerField(default=0)
    impact_armor = models.IntegerField(default=0)
    ballistic_armor = models.IntegerField(default=0)


class MovementAbility(models.Model):
    type = models.CharField(choices=MOVEMENT_TYPE_CHOICES, max_length=100)
    on_all_four = models.BooleanField(default=False)
    distance = models.IntegerField(default=0)


class Ability(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class DeltaStats(models.Model):
    """
    A container for most of the common bonuses
    """
    attributes = models.OneToOneField(
        DeltaAttributes,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='DeltaStats'
    )
    body = models.OneToOneField(
        DeltaBody,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='DeltaStats'
    )
    skills = models.ManyToManyField(
        DeltaSkill,
        blank=True
    )
    defence = models.OneToOneField(
        DeltaDefence,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='DeltaStats'
    )
    movement_ability = models.OneToOneField(
        MovementAbility,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='DeltaStats'
    )

    def get_parent_name(self):
        if hasattr(self, 'UpliftedType'):
            return 'Uplifted type', self.UpliftedType.name
        elif hasattr(self, 'HeritageTrait'):
            return 'Heritage Trait', self.HeritageTrait.name
        elif hasattr(self, 'HeritageDrawback'):
            return 'Heritage Drawback', self.HeritageDrawback.name
        else:
            return "Unassigned", "unassigned"

    def __str__(self):
        parent_type, parent_name = self.get_parent_name()
        return parent_type + ": " + parent_name + " - DeltaStats"


class Heritage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    free_traits = models.IntegerField()
    trait_with_drawback = models.IntegerField()

    def __str__(self):
        return self.name


class HeritageTrait(models.Model):
    name = models.CharField(max_length=100)
    heritage = models.ForeignKey(Heritage, on_delete=models.PROTECT)
    description = models.TextField()
    delta_stats = models.OneToOneField(DeltaStats, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.heritage.name + ": " + self.name


class HeritageDrawback(models.Model):
    name = models.CharField(max_length=100)
    heritage = models.ForeignKey(Heritage, on_delete=models.PROTECT)
    description = models.TextField()
    delta_stats = models.OneToOneField(DeltaStats, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.heritage.name + ": " + self.name


class UpliftedType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    attribute_cost = models.IntegerField(default=0)
    small = models.BooleanField()
    delta_stats = models.OneToOneField(DeltaStats, on_delete=models.PROTECT, null=True)

    trait = models.ForeignKey(HeritageTrait, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.name


class MagicAbilities(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Lifestyle(models.Model):
    name = models.CharField(max_length=100)
    rent = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class KnowledgeTopic(models.Model):
    name = models.CharField(max_length=100)
    official = models.BooleanField(default=False)


class KnowledgeSkillValue(models.Model):
    character = models.ForeignKey('Character', models.CASCADE)
    topic = models.ForeignKey(KnowledgeTopic, models.PROTECT)
    value = models.IntegerField(default=0)


class Character(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,  blank=True, null=True)
    created = models.BooleanField(default=False)

    # Assets
    # TODO Ghost Rating
    # TODO cash = models.IntegerField(default=0)
    # TODO Lifestyle
    # TODO brand = models.ForeignKey(Brand)

    # Attribute
    strength = models.IntegerField(default=1)
    body = models.IntegerField(default=1)
    reaction = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)
    willpower = models.IntegerField(default=1)
    charisma = models.IntegerField(default=1)

    # Special attributes
    zoetic_potential = models.IntegerField(default=6)   # TODO figure out system
    melee_reach_base = models.IntegerField(default=0)
    movement_distance_base = models.IntegerField(default=6)
    condition_physical = models.IntegerField(default=6)
    condition_stun = models.IntegerField(default=6)
    """
        All humans (including the green and the blighted) start with a Zoetic Potential of 6. Uplifted animals start 
        with a Zoetic Potential of 5 due to their baseline implants. Synthetics start with a Zoetic Potential of 1.
    """
    heritage = models.ForeignKey(Heritage, on_delete=models.PROTECT, blank=True, null=True)
    uplifted_type = models.ForeignKey(UpliftedType, on_delete=models.PROTECT, blank=True, null=True)
    heritage_trait_1 = models.ForeignKey(HeritageTrait, on_delete=models.PROTECT, blank=True, null=True, related_name="heritage_trait_1")
    heritage_trait_2 = models.ForeignKey(HeritageTrait, on_delete=models.PROTECT, blank=True, null=True, related_name="heritage_trait_2")
    heritage_trait_3 = models.ForeignKey(HeritageTrait, on_delete=models.PROTECT, blank=True, null=True, related_name="heritage_trait_3")
    heritage_drawback = models.ForeignKey(HeritageDrawback, on_delete=models.PROTECT, blank=True, null=True)

    magic_ablity = models.ForeignKey(MagicAbilities, on_delete=models.PROTECT, blank=True, null=True)

    # Active skill
    # Brawn Pool
    melee_weapons = models.IntegerField(default=0)
    unarmed_combat = models.IntegerField(default=0)
    martial_arts = models.IntegerField(default=0)
    throwing_weapons = models.IntegerField(default=0)
    cybertechtronic_combat = models.IntegerField(default=0)
    athletics = models.IntegerField(default=0)

    # Finesse Pool
    firearms = models.IntegerField(default=0)
    gunnery = models.IntegerField(default=0)
    heavy_weapons = models.IntegerField(default=0)
    energy_weapons = models.IntegerField(default=0)
    archery = models.IntegerField(default=0)
    articulated_maneuvers = models.IntegerField(default=0)

    # Focus Pool
    shadow = models.IntegerField(default=0)
    drive = models.IntegerField(default=0)
    fly = models.IntegerField(default=0)
    observation = models.IntegerField(default=0)
    biotech = models.IntegerField(default=0)
    reconnaissance = models.IntegerField(default=0)
    locksmith = models.IntegerField(default=0)
    computer_hacking = models.IntegerField(default=0)
    computer_electronic_warfare = models.IntegerField(default=0)
    computer_programming = models.IntegerField(default=0)
    engineering_mechanical = models.IntegerField(default=0)
    engineering_industrial = models.IntegerField(default=0)
    engineering_aeronautics = models.IntegerField(default=0)
    engineering_armory = models.IntegerField(default=0)
    engineering_nautical = models.IntegerField(default=0)
    artificing = models.IntegerField(default=0)
    negotiations = models.IntegerField(default=0)

    # Resolve pool
    rituals = models.IntegerField(default=0)
    channeling = models.IntegerField(default=0)
    sorcery = models.IntegerField(default=0)
    astral_senses = models.IntegerField(default=0)
    survival = models.IntegerField(default=0)
    conjuring = models.IntegerField(default=0)
    leadership = models.IntegerField(default=0)
    subterfuge = models.IntegerField(default=0)
    coercion = models.IntegerField(default=0)
    fascination = models.IntegerField(default=0)

    # Knowledge Skill
    # TODO
    # Etiquette skill
    corporate_etiquette = models.IntegerField(default=0)
    street_etiquette = models.IntegerField(default=0)
    civic_etiquette = models.IntegerField(default=0)
    aristocratic_etiquette = models.IntegerField(default=0)
    military_etiquette = models.IntegerField(default=0)
    criminal_etiquette = models.IntegerField(default=0)
    wasteland_etiquette = models.IntegerField(default=0)

    def __str__(self):
        return self.name