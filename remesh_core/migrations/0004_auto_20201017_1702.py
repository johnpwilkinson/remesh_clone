# Generated by Django 3.1.2 on 2020-10-17 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('remesh_core', '0003_messages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Messages',
            new_name='Message',
        ),
    ]