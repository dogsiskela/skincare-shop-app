# Generated by Django 4.2.4 on 2023-08-26 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_seller',
            field=models.BooleanField(default=False),
        ),
    ]
