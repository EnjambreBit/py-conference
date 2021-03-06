# Generated by Django 3.2 on 2022-06-07 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("conferences", "0032_auto_20220607_0031"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="call_for_papers_page",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="events_cfp_page",
                to="conferences.staticpage",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="location_content",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="events_location",
                to="conferences.staticpage",
            ),
        ),
    ]
