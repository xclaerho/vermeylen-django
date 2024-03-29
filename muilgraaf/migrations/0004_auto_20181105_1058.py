# Generated by Django 2.1.2 on 2018-11-05 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('muilgraaf', '0003_auto_20181105_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_person', to='muilgraaf.Person', verbose_name='Persoon 1'),
        ),
        migrations.AlterField(
            model_name='link',
            name='sid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_person', to='muilgraaf.Person', verbose_name='Persoon 2'),
        ),
    ]
