# Generated by Django 5.1.1 on 2024-10-30 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="description",
            field=models.TextField(max_length=666, verbose_name="书籍简介"),
        ),
    ]