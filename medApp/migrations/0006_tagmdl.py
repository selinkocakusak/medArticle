# Generated by Django 3.2.4 on 2021-06-21 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medApp', '0005_retrieve_save'),
    ]

    operations = [
        migrations.CreateModel(
            name='tagMdl',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('docId', models.CharField(blank=True, max_length=20)),
                ('tag', models.CharField(max_length=30)),
                ('link', models.URLField(max_length=250)),
            ],
        ),
    ]
