# Generated by Django 2.2 on 2021-08-28 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210603_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='publish_date',
            field=models.DateTimeField(auto_now=True),
            preserve_default=False,
        ),
    ]
