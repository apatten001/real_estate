# Generated by Django 2.1.2 on 2018-10-16 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0005_auto_20181011_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homelisting',
            name='img',
            field=models.ImageField(blank=True, default='default_home.png', null=True, upload_to='house_photos'),
        ),
    ]
