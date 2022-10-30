# Generated by Django 3.2.16 on 2022-10-30 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stash', '0004_auto_20221029_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('material_type', models.CharField(choices=[('WO', 'Wool'), ('WP', 'Alpaca'), ('WS', 'Cashmere')], default='WO', max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='yarn',
            name='material',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='stash.material'),
        ),
    ]
