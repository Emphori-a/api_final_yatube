# Generated by Django 3.2.16 on 2024-02-13 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_follow_unique_user_following'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_user_following',
        ),
    ]
