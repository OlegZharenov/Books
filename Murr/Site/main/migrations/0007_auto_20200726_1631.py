# Generated by Django 3.0.8 on 2020-07-26 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200723_1546'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Tag',
        ),
    ]
