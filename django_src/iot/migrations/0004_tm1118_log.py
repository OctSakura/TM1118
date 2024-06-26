# Generated by Django 5.0 on 2024-04-16 04:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("iot", "0003_event_time"),
    ]

    operations = [
        migrations.CreateModel(
            name="tm1118_log",
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
                ("node_id", models.TextField()),
                ("loc", models.TextField()),
                ("temp", models.IntegerField()),
                ("hum", models.IntegerField()),
                ("light", models.IntegerField()),
                ("snd", models.IntegerField()),
                ("time", models.TextField()),
            ],
        ),
    ]
