# Generated by Django 4.1.6 on 2023-05-23 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_quizattempt_otp_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizuserscore',
            name='quiz_domain',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
