# Generated by Django 3.2.16 on 2022-11-07 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stash', '0026_rename_color_yarn_color_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='yarn',
            name='frogged',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
