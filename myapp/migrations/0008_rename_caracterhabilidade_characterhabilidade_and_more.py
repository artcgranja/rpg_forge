# Generated by Django 5.1.3 on 2024-11-29 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_naturezarpg_rename_tiposhabilidade_efeitorpg_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CaracterHabilidade',
            new_name='CharacterHabilidade',
        ),
        migrations.RenameModel(
            old_name='CaracterItem',
            new_name='CharacterItem',
        ),
        migrations.RenameModel(
            old_name='CaracterRPG',
            new_name='CharacterRPG',
        ),
    ]
