# Generated by Django 2.1.2 on 2018-11-14 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('augustjes', '0003_auto_20181105_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='augustje',
            name='date',
            field=models.DateField(verbose_name='datum'),
        ),
        migrations.AlterField(
            model_name='augustje',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='beschrijving'),
        ),
        migrations.AlterField(
            model_name='augustje',
            name='edition',
            field=models.CharField(max_length=50, verbose_name='editie'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='name',
            field=models.CharField(max_length=50, verbose_name='naam'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='room',
            field=models.IntegerField(blank=True, null=True, verbose_name='kamer'),
        ),
    ]