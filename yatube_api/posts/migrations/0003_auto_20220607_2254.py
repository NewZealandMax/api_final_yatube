# Generated by Django 2.2.16 on 2022-06-07 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220605_2313'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_following',
        ),
    ]
