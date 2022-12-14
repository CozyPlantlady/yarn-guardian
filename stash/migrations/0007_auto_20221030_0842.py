# Generated by Django 3.2.16 on 2022-10-30 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stash', '0006_auto_20221030_0816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_choice', models.CharField(choices=[('1', 'White'), ('2', 'Yellow'), ('3', 'Blue'), ('4', 'Red'), ('5', 'Green'), ('6', 'Black'), ('7', 'Brown')], default='1', max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='yarn',
            name='color',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='stash.color'),
        ),
    ]
