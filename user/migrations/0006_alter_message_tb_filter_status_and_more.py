# Generated by Django 4.1 on 2022-12-22 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_message_tb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message_tb',
            name='filter_status',
            field=models.CharField(default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='message_tb',
            name='status',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]