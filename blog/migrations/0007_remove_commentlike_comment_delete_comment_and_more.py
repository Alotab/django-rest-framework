# Generated by Django 4.2.3 on 2024-12-23 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_posts_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentlike',
            name='comment',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='CommentLike',
        ),
    ]
