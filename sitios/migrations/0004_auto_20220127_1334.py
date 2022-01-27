# Generated by Django 3.2 on 2022-01-27 13:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0003_auto_20220127_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sedesclinica',
            name='fechaRegistro',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='sedesclinica',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]