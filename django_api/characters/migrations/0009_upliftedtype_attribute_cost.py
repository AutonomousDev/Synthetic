# Generated by Django 5.0.3 on 2024-03-12 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0008_remove_activeskillvalue_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='upliftedtype',
            name='attribute_cost',
            field=models.IntegerField(default=0),
        ),
    ]
