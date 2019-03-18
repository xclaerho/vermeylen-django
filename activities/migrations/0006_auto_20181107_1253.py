# Generated by Django 2.1.2 on 2018-11-07 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0005_auto_20181107_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='facebooklink',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='Facebook link'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='googlecalendarlink',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='Google calendar link'),
        ),
    ]