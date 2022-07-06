# Generated by Django 3.2 on 2022-06-19 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0036_auto_20220619_1703'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventlink',
            options={'ordering': ['order'], 'verbose_name': 'EventLink', 'verbose_name_plural': 'Event links'},
        ),
        migrations.AddField(
            model_name='eventlink',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]