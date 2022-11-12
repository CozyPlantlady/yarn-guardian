# Generated by Django 3.2.16 on 2022-11-12 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stash', '0033_auto_20221111_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yarn',
            name='amount',
            field=models.IntegerField(blank=True, default='', null=True, verbose_name='How much yarn you have?'),
        ),
        migrations.AlterField(
            model_name='yarn',
            name='body',
            field=models.TextField(blank=True, verbose_name='Notes about the yarn:'),
        ),
        migrations.AlterField(
            model_name='yarn',
            name='color_code',
            field=models.CharField(blank=True, default='', max_length=6, verbose_name="Producer's color code"),
        ),
        migrations.AlterField(
            model_name='yarn',
            name='color_name',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Color name'),
        ),
        migrations.AlterField(
            model_name='yarn',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='Name of the Yarn'),
        ),
        migrations.AlterField(
            model_name='yarn',
            name='producer',
            field=models.CharField(max_length=50, verbose_name="Producer's name"),
        ),
    ]
