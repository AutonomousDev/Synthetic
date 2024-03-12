# Generated by Django 5.0.3 on 2024-03-11 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0004_rename_activeskills_activeskill'),
    ]

    operations = [
        migrations.AddField(
            model_name='activeskill',
            name='dice_pool',
            field=models.CharField(choices=[('Brawn Pool', 'Brawn Pool'), ('Finesse Pool', 'Finesse Pool'), ('Focus Pool', 'Focus Pool'), ('Resolve Pool', 'Resolve Pool')], default='Brawn Pool', max_length=100),
            preserve_default=False,
        ),
    ]
