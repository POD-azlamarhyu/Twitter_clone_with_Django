# Generated by Django 3.2.3 on 2021-06-04 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0006_alter_tweet_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='value',
        ),
    ]