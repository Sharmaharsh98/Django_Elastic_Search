# Generated by Django 4.2.1 on 2023-05-21 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alphabets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alphabet', models.CharField(max_length=10)),
                ('word', models.CharField(max_length=50)),
            ],
        ),
    ]
