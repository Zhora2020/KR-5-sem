# Generated by Django 4.1.1 on 2022-12-09 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raceclub_app', '0009_raceclub_characteristic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('nickname', models.CharField(max_length=10)),
                ('feedback', models.TextField()),
                ('rating', models.PositiveIntegerField()),
            ],
        ),
    ]
