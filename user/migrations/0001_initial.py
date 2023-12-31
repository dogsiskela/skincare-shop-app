# Generated by Django 4.2.4 on 2023-08-26 16:49

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('sys_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=127, unique=True)),
                ('is_staff', models.BooleanField()),
                ('is_seller', models.BooleanField()),
            ],
            options={
                'db_table': 'users',
            },
            managers=[
                ('objects', user.models.MyUserManager()),
            ],
        ),
    ]
