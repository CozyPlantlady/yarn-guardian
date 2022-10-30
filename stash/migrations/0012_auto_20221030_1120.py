# Generated by Django 3.2.16 on 2022-10-30 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stash', '0011_auto_20221030_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='yarn',
            name='body',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='yarn',
            name='amount',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='stash.amount'),
        ),
    ]
