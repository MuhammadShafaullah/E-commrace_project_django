# Generated by Django 4.1 on 2022-11-22 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usersignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('contactnum', models.CharField(max_length=12)),
                ('postadress', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
    ]