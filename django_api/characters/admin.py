from django.contrib import admin
from characters.models import (
    ActiveSkillGroup,
    ActiveSkill,
    ActiveSkillValue,
    Heritage,
    HeritageTrait,
    HeritageDrawback,
    UpliftedType,
    MagicAbilities,
    Lifestyle,
    Character,
    DeltaAttributes,
    DeltaBody
)


admin.site.register(ActiveSkillGroup)
admin.site.register(ActiveSkill)
admin.site.register(ActiveSkillValue)
admin.site.register(Heritage)
admin.site.register(HeritageTrait)
admin.site.register(HeritageDrawback)
admin.site.register(UpliftedType)
admin.site.register(MagicAbilities)
admin.site.register(Lifestyle)
admin.site.register(Character)
admin.site.register(DeltaAttributes)
admin.site.register(DeltaBody)
