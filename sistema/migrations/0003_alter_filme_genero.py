# Generated by Django 5.1.7 on 2025-03-31 17:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0002_filme_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='genero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sistema.genero'),
        ),
    ]
