# Generated by Django 3.2 on 2022-08-17 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("conferences", "0041_alter_talk_talk_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="TalkRegistration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="talks_registrations_profile",
                        to="conferences.profile",
                    ),
                ),
                (
                    "talk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="talks_registrations",
                        to="conferences.talk",
                    ),
                ),
            ],
            options={
                "verbose_name": "Talk Registration",
                "verbose_name_plural": "Talk Registrations",
                "db_table": "talk_registrations",
            },
        ),
    ]
