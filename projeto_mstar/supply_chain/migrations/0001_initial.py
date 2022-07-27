# Generated by Django 4.0.6 on 2022-07-26 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Mercadoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro', models.IntegerField(unique=True)),
                ('nome', models.CharField(max_length=250)),
                ('fabricante', models.CharField(max_length=250)),
                ('tipo', models.CharField(max_length=250)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Saida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('data', models.DateTimeField()),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supply_chain.local')),
                ('mercadoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supply_chain.mercadoria')),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('data', models.DateTimeField()),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supply_chain.local')),
                ('mercadoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supply_chain.mercadoria')),
            ],
        ),
    ]
