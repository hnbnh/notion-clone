# Generated by Django 3.2.11 on 2022-08-10 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_page_closed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='closed',
            field=models.BooleanField(default=True),
        ),
    ]