# Generated by Django 4.0.4 on 2022-06-23 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='herramienta',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='imagenes/')),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pinturas',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('color', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='imagenes/')),
                ('cantidad', models.IntegerField()),
            ],
        ),
    ]
