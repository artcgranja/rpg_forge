# Generated by Django 5.1.3 on 2024-11-29 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_caracterrpg_mana_caracterrpg_vida_caracterrpg_vivo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='caracterrpg',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]