# Generated by Django 3.2 on 2022-01-28 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_auto_20220128_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='documento',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
