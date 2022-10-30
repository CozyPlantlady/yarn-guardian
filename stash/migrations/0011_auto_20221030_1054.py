# Generated by Django 3.2.16 on 2022-10-30 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stash', '0010_alter_material_material_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_type', models.CharField(choices=[('0', 'Lace'), ('1', 'Super Fine'), ('2', 'Fine'), ('3', 'Light'), ('4', 'Medium'), ('5', 'Bulky'), ('6', 'Super Bulky')], default='3', max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='yarn',
            name='weight',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='stash.weight'),
        ),
    ]