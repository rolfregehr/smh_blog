# Generated by Django 5.1.1 on 2024-10-05 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='sobrenome',
            field=models.CharField(max_length=100, verbose_name='Sobrenome'),
        ),
    ]
