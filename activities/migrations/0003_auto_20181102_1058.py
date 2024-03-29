# Generated by Django 2.1.2 on 2018-11-02 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_auto_20181101_1832'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name': 'activiteit', 'verbose_name_plural': 'activiteiten'},
        ),
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.TextField(blank=True, verbose_name='beschrijving'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='end',
            field=models.DateTimeField(verbose_name='Einde'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='facebooklink',
            field=models.CharField(blank=True, max_length=200, verbose_name='Facebook link'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='location',
            field=models.CharField(blank=True, max_length=50, verbose_name='Locatie'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(max_length=50, verbose_name='naam'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='price',
            field=models.FloatField(default=0, verbose_name='Prijs'),
        ),
    ]
