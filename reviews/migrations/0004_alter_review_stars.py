# Generated by Django 4.1 on 2022-12-21 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0003_alter_review_stars"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="stars",
            field=models.IntegerField(),
        ),
    ]
