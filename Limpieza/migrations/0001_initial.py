# Generated by Django 4.1.3 on 2022-11-29 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cepillos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('proveedor', models.CharField(max_length=50)),
                ('prodxbulto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='descartables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('proveedor', models.CharField(max_length=50)),
                ('prodxbulto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='quimicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('proveedor', models.CharField(max_length=50)),
                ('prodxbulto', models.IntegerField()),
            ],
        ),
    ]
