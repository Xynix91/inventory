# Generated by Django 3.0 on 2020-04-16 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20200413_0440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='films', to='inventory.User'),
        ),
    ]
