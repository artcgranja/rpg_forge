# Generated by Django 5.1.3 on 2024-11-29 17:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_habilidade_item_tiposhabilidade_caracterhabilidade_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NaturezaRPG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='TiposHabilidade',
            new_name='EfeitoRPG',
        ),
        migrations.RenameField(
            model_name='habilidade',
            old_name='tipo',
            new_name='efeito',
        ),
        migrations.AddField(
            model_name='habilidade',
            name='acao_extra',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='habilidade',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='habilidades/'),
        ),
        migrations.AddField(
            model_name='habilidade',
            name='valor',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='acao_extra',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='efeito',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='myapp.efeitorpg'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='gasto_de_mana',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='itens/'),
        ),
        migrations.AddField(
            model_name='item',
            name='valor',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='CaracterItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caracter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.caracterrpg')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.item')),
            ],
        ),
        migrations.AddField(
            model_name='habilidade',
            name='natureza',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='myapp.naturezarpg'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='natureza',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='myapp.naturezarpg'),
            preserve_default=False,
        ),
    ]
