# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-08 22:58


from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('office_hours', models.CharField(max_length=70)),
                ('photo1_url', models.CharField(max_length=255)),
                ('photo2_url', models.CharField(max_length=255)),
                ('blurb', models.CharField(max_length=255)),
                ('pb_position', models.CharField(max_length=255)),
            ],
        ),
    ]