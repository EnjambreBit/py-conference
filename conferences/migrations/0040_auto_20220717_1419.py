# Generated by Django 3.2 on 2022-07-17 17:19

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0039_alter_talk_talk_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resourcefile',
            name='file',
            field=models.FileField(default=None, null=True, upload_to='resources/'),
        ),
        migrations.AlterField(
            model_name='resourceimage',
            name='photo',
            field=sorl.thumbnail.fields.ImageField(default=None, null=True, upload_to='resources/'),
        ),
        migrations.AlterField(
            model_name='resourcelink',
            name='url',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
