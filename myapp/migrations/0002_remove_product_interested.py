# Generated by Django 2.2.1 on 2019-06-07 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='interested',
        ),
    ]
