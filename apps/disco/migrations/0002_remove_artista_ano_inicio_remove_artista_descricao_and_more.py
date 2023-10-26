# Generated by Django 4.2.2 on 2023-10-24 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disco', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artista',
            name='ano_inicio',
        ),
        migrations.RemoveField(
            model_name='artista',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='artista',
            name='genero',
        ),
        migrations.RemoveField(
            model_name='artista',
            name='pais',
        ),
        migrations.RemoveField(
            model_name='selo_fonografico',
            name='pais',
        ),
        migrations.AddField(
            model_name='disco',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
    ]