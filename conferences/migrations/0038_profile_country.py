# Generated by Django 3.2 on 2022-06-20 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("conferences", "0037_auto_20220619_1707"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="country",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="conferences.country",
            ),
        ),
    ]
