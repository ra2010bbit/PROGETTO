# Generated by Django 5.0.3 on 2024-05-09 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("progetto_macchine", "0003_customuser"),
    ]

    operations = [
        migrations.AlterField(
            model_name="machineimage",
            name="image",
            field=models.ImageField(upload_to="media/machine_photos"),
        ),
    ]
