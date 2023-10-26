# Generated by Django 4.2.2 on 2023-10-23 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField(max_length=255)),
                ('ano_inicio', models.IntegerField()),
                ('pais', models.CharField(max_length=150)),
                ('genero', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Selo_Fonografico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('pais', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Disco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField(max_length=255)),
                ('ano', models.IntegerField()),
                ('pais', models.CharField(max_length=150)),
                ('genero', models.CharField(max_length=150)),
                ('quantidade', models.IntegerField()),
                ('artistas', models.ManyToManyField(to='disco.artista')),
                ('selo_fonografico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disco.selo_fonografico')),
            ],
        ),
    ]