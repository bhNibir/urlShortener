# Generated by Django 2.2 on 2019-04-29 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_auto_20190429_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortenurl',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]