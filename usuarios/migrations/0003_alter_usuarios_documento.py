# Generated by Django 3.2 on 2022-01-28 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20220127_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='documento',
            field=models.IntegerField(unique=True),
        ),
    ]