# Generated by Django 2.1.2 on 2019-01-16 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrequentQuestionsAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='frequentquestions',
            name='answer',
        ),
        migrations.AddField(
            model_name='frequentquestionsanswers',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faqs.FrequentQuestions'),
        ),
    ]
