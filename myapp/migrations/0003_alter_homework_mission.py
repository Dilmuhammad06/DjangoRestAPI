# Generated by Django 5.0.2 on 2024-03-01 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_homework'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='mission',
            field=models.CharField(max_length=255),
        ),
    ]
