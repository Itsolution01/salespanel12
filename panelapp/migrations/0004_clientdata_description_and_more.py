# Generated by Django 5.1.1 on 2024-09-20 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("panelapp", "0003_userclientinteraction"),
    ]

    operations = [
        migrations.AddField(
            model_name="clientdata",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="userclientinteraction",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="usersubmits",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]