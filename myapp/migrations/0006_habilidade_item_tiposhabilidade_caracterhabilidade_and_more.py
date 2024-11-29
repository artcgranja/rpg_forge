# Generated by Django 5.1.3 on 2024-11-29 03:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_caracterrpg_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TiposHabilidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CaracterHabilidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caracter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.caracterrpg')),
                ('habilidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.habilidade')),
            ],
        ),
        migrations.AddField(
            model_name='habilidade',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.tiposhabilidade'),
        ),
    ]