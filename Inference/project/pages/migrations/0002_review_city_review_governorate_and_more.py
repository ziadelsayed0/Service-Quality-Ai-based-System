# Generated by Django 4.2.2 on 2023-06-24 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='City',
            field=models.TextField(default='NA', max_length=10),
        ),
        migrations.AddField(
            model_name='review',
            name='Governorate',
            field=models.TextField(default='NA', max_length=10),
        ),
        migrations.AddField(
            model_name='review',
            name='Important_Topics',
            field=models.TextField(default='NA', max_length=30),
        ),
        migrations.AddField(
            model_name='review',
            name='Sector',
            field=models.TextField(default='NA', max_length=10),
        ),
        migrations.AddField(
            model_name='review',
            name='Subject',
            field=models.TextField(default='NA', max_length=20),
        ),
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(default='NA', max_length=1000),
        ),
    ]
