# Generated by Django 4.1.1 on 2022-09-10 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_andao_atakalo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toy',
            name='token',
        ),
    ]