# Generated by Django 2.1.2 on 2019-01-16 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0009_frequentquestions'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='FrequentQuestions',
        ),
    ]
