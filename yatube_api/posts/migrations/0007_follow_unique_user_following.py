# Generated by Django 3.2.16 on 2024-02-13 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_remove_follow_unique_user_following'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user_id', 'following_id'), name='unique_user_following'),
        ),
    ]