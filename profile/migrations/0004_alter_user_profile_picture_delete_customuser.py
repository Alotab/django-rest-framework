# Generated by Django 4.2.3 on 2024-12-13 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0003_rename_profile_image_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
