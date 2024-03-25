# Generated by Django 5.0.3 on 2024-03-09 03:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="lectures",
            name="video",
        ),
        migrations.AddField(
            model_name="lectures",
            name="link",
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
