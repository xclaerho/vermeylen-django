# Generated by Django 2.1.2 on 2018-11-05 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('augustjes', '0002_auto_20181105_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='room',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]