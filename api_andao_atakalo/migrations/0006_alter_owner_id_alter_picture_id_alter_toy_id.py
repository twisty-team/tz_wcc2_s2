# Generated by Django 4.1.1 on 2022-09-10 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_andao_atakalo', '0005_alter_owner_id_alter_picture_id_alter_toy_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='picture',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='toy',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]