# Generated by Django 4.2.2 on 2023-06-25 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_review_city_review_governorate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='Recommended_action',
            field=models.TextField(default='NA', max_length=2000),
        ),
    ]
