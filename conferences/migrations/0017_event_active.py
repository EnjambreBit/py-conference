# Generated by Django 3.2 on 2022-04-18 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0016_auto_20220418_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]