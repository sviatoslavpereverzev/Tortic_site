# Generated by Django 2.1.2 on 2018-10-22 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('torticapp', '0004_auto_20181020_1105'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stuffing',
            new_name='Slides',
        ),
        migrations.AlterModelOptions(
            name='slides',
            options={'verbose_name': 'Slide', 'verbose_name_plural': 'Slides'},
        ),
    ]