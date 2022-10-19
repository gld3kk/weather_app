# Generated by Django 4.1.2 on 2022-10-19 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City_Weather",
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
                ("city_state", models.CharField(max_length=200)),
                ("temperature_low", models.TextField()),
                ("temperature_high", models.TextField()),
                ("weather_main", models.TextField()),
                ("weather_description", models.TextField()),
            ],
        ),
    ]