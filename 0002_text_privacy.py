# Generated by Django 4.1 on 2022-09-15 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='privacy',
            field=models.BooleanField(default=True),
        ),
    ]
