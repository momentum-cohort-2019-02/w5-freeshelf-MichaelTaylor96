# Generated by Django 2.1.7 on 2019-03-14 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20190313_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=None),
            preserve_default=False,
        ),
    ]
