# Generated by Django 4.2.6 on 2023-12-05 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('hobbies', models.CharField(max_length=100)),
                ('favorite_music', models.CharField(max_length=100)),
            ],
        ),
    ]