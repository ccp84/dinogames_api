# Generated by Django 3.2.19 on 2023-05-24 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_remove_game_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='overview',
            field=models.TextField(blank=True),
        ),
    ]
