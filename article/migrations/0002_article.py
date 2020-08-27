# Generated by Django 3.0.3 on 2020-08-08 18:45

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=30)),
                ('image_link', models.CharField(max_length=1000)),
                ('content', ckeditor.fields.RichTextField()),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
