# Generated by Django 3.1.7 on 2021-03-06 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sorting', '0002_auto_20210306_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addsorting',
            name='input_file',
        ),
        migrations.RemoveField(
            model_name='addsorting',
            name='output_file',
        ),
    ]