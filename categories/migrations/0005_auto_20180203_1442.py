# Generated by Django 2.0.1 on 2018-02-03 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_auto_20180122_0743'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id']},
        ),
    ]
