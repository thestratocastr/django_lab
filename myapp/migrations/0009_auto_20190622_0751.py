# Generated by Django 2.2.1 on 2019-06-22 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20190622_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='image',
            field=models.FileField(blank=True, upload_to='static/client_pic/'),
        ),
    ]
