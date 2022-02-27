# Generated by Django 3.2.12 on 2022-02-27 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PesoDolar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso_dolar', models.FloatField()),
                ('peso_dolar_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TIE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tie', models.FloatField()),
                ('tie_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UDI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('udi', models.FloatField()),
                ('udi_date', models.DateTimeField()),
            ],
        ),
    ]
