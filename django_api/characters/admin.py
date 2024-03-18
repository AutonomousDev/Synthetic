from django.contrib import admin
from characters.models import (
    ActiveSkillGroup,
    ActiveSkill,
    Heritage,
    HeritageTrait,
    HeritageDrawback,
    UpliftedType,
    MagicAbilities,
    Lifestyle,
    Character,
    DeltaAttributes,
    DeltaBody,
    DeltaSkill
)


admin.site.register(ActiveSkillGroup)
admin.site.register(ActiveSkill)
admin.site.register(Heritage)
admin.site.register(HeritageTrait)
admin.site.register(HeritageDrawback)
admin.site.register(UpliftedType)
admin.site.register(MagicAbilities)
admin.site.register(Lifestyle)
admin.site.register(Character)
admin.site.register(DeltaAttributes)
admin.site.register(DeltaBody)
admin.site.register(DeltaSkill)
