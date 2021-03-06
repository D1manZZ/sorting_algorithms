# Generated by Django 3.1.7 on 2021-03-06 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorting', '0004_addsorting_sort_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addsorting',
            name='sort_file',
        ),
        migrations.AddField(
            model_name='addsorting',
            name='sort_result',
            field=models.TextField(default='none', verbose_name='результат'),
        ),
        migrations.AlterField(
            model_name='sortingform',
            name='input_file',
            field=models.FileField(upload_to='', verbose_name='исходный файл'),
        ),
    ]
