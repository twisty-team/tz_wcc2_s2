# Generated by Django 4.1.1 on 2022-09-10 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_andao_atakalo', '0006_alter_owner_id_alter_picture_id_alter_toy_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Toy',
            new_name='Exchange',
        ),
    ]