# Generated by Django 4.1 on 2022-12-28 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_contact_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='blacklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('remarks', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('contactid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blacklistedcontact', to='user.user_register_tb')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to='user.user_register_tb')),
            ],
        ),
    ]
