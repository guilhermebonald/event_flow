# Generated by Django 4.2.7 on 2024-01-30 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_rename_usuario_eventmodel_user_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EventModel',
        ),
    ]