# Generated by Django 2.1.2 on 2018-10-11 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0004_homelisting_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homelisting',
            name='zip_code',
            field=models.CharField(max_length=9),
        ),
    ]
