# Generated by Django 5.1 on 2024-08-08 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0002_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SLNo', models.IntegerField()),
                ('DistrictName', models.CharField(max_length=100)),
                ('Population', models.IntegerField()),
                ('Area', models.IntegerField()),
            ],
        ),
    ]
