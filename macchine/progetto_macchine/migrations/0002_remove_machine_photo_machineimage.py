# Generated by Django 5.0.3 on 2024-05-01 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("progetto_macchine", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="machine",
            name="photo",
        ),
        migrations.CreateModel(
            name="MachineImage",
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
                ("image", models.ImageField(upload_to="machine_photos")),
                (
                    "machine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="progetto_macchine.machine",
                    ),
                ),
            ],
        ),
    ]
