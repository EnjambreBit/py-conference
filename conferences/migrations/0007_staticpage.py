# Generated by Django 3.2 on 2022-03-01 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("conferences", "0006_auto_20220301_0243"),
    ]

    operations = [
        migrations.CreateModel(
            name="StaticPage",
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
                    "title",
                    models.CharField(
                        blank=True, default=None, max_length=200, null=True
                    ),
                ),
                ("content", models.TextField(blank=True, default=None, null=True)),
                (
                    "format",
                    models.TextField(
                        choices=[
                            ("html", "HTML"),
                            ("txt", "Plain Text"),
                            ("md", "Markdown"),
                        ],
                        default="txt",
                        max_length=4,
                    ),
                ),
                ("published", models.BooleanField(default=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("last_update", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "StaticPage",
                "verbose_name_plural": "static_pages",
                "db_table": "static_pages",
            },
        ),
    ]
