# Generated by Django 3.2.7 on 2021-09-10 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20210910_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='pixelcount',
            name='black_or_white',
            field=models.CharField(default='equal', max_length=5),
            preserve_default=False,
        ),
    ]
