# Generated by Django 4.2.3 on 2024-12-08 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_user_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='profile_image',
            new_name='profile_picture',
        ),
    ]
