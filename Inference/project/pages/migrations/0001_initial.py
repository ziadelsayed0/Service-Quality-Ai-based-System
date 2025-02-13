# Generated by Django 4.2.2 on 2023-06-24 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=1000)),
                ('Sentiment_type', models.TextField(default='NA', max_length=20)),
                ('Topic', models.TextField(default='NA', max_length=30)),
                ('Recommended_action', models.TextField(default='NA', max_length=1000)),
            ],
            options={
                'verbose_name': 'review',
            },
        ),
    ]
