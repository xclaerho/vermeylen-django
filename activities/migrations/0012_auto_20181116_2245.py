# Generated by Django 2.1.3 on 2018-11-16 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0011_auto_20181116_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='addtocalendar',
            field=models.BooleanField(default=False, help_text='Door praeses aan te klikken wanneer het aan de calendar toegevoegd mag worden.', verbose_name='toegevoegd aan Google calendar?'),
        ),
    ]
