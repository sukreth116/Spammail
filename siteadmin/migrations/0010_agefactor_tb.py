# Generated by Django 4.1 on 2022-12-22 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0009_alter_seasoncountry_tb_months'),
    ]

    operations = [
        migrations.CreateModel(
            name='agefactor_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minimum_age', models.IntegerField(max_length=20)),
                ('maximum_age', models.IntegerField(max_length=20)),
                ('age_factor', models.CharField(max_length=20)),
            ],
        ),
    ]
