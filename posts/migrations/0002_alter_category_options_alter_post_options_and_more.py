# Generated by Django 4.2.7 on 2024-05-28 12:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "category", "verbose_name_plural": "categories"},
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"verbose_name": "post", "verbose_name_plural": "posts"},
        ),
        migrations.AlterModelOptions(
            name="tag",
            options={"verbose_name": "tag", "verbose_name_plural": "tags"},
        ),
    ]
