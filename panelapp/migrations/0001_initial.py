# Generated by Django 5.1.1 on 2024-09-16 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ClientData",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phonenumber", models.CharField(max_length=15)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("investigate_date", models.DateField(blank=True, null=True)),
                ("schedule_date", models.DateField(blank=True, null=True)),
                ("lead", models.CharField(max_length=100)),
                ("response", models.TextField()),
                ("assigned_user", models.CharField(max_length=15)),
            ],
        ),
    ]
