# Generated by Django 2.2 on 2019-04-29 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0005_auto_20190429_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortenurl',
            name='add_date',
            field=models.DateTimeField(),
        ),
    ]