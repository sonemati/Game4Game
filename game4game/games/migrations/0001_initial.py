# Generated by Django 4.1 on 2023-04-30 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Game",
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
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField(allow_unicode=True, unique=True)),
                ("genre", models.CharField(blank=True, max_length=100)),
                ("platform", models.CharField(blank=True, max_length=100)),
                ("release_date", models.DateField(blank=True, default="")),
                ("description", models.TextField(blank=True, default="")),
                ("game_pic", models.ImageField(blank=True, upload_to="game_pics")),
            ],
            options={"ordering": ["name"],},
        ),
    ]
