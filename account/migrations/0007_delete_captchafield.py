# Generated by Django 3.2 on 2023-07-07 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20230707_1401'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CaptchaField',
        ),
    ]
