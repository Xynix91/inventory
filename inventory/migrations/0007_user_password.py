# Generated by Django 3.0 on 2020-04-20 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20200416_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=123, max_length=250),
            preserve_default=False,
        ),
    ]
