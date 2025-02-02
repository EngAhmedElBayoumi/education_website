# Generated by Django 5.0.3 on 2024-03-08 07:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=100)),
                ("author", models.CharField(max_length=100)),
                ("image", models.ImageField(blank=True, upload_to="books")),
                ("pages", models.IntegerField()),
                ("file", models.FileField(blank=True, upload_to="books")),
            ],
        ),
    ]
