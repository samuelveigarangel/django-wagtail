# Generated by Django 4.1.3 on 2022-11-18 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_homepage_banner_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="teste",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
