# Generated by Django 2.1.2 on 2018-10-11 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_auto_20181010_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='homelisting',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='homelisting',
            name='img',
            field=models.ImageField(upload_to='house_photos'),
        ),
    ]
