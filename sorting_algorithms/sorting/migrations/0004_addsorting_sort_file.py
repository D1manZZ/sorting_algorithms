# Generated by Django 3.1.7 on 2021-03-06 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorting', '0003_auto_20210306_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='addsorting',
            name='sort_file',
            field=models.FileField(blank=True, upload_to='files_inputs', verbose_name='файл сортировки'),
        ),
    ]
