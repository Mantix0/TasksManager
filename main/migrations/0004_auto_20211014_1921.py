# Generated by Django 3.2.8 on 2021-10-14 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_city'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.AddField(
            model_name='task',
            name='date_time',
            field=models.DateTimeField(default=3, verbose_name='Дата'),
            preserve_default=False,
        ),
    ]
