# Generated by Django 3.2.2 on 2021-05-30 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210530_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='/avatar.png', upload_to='avatar/%Y/%m/%d'),
        ),
    ]
