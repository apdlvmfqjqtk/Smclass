# Generated by Django 5.1.3 on 2024-11-21 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('pw', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=30)),
                ('birth', models.CharField(max_length=50)),
                ('gender', models.CharField(default='남성', max_length=5)),
                ('news', models.CharField(default='예', max_length=5)),
                ('sms', models.CharField(default='예', max_length=5)),
                ('memnum', models.CharField(max_length=8)),
                ('memaaa', models.IntegerField(max_length=4)),
                ('job', models.CharField(max_length=10)),
                ('married', models.CharField(max_length=5)),
                ('hobby', models.CharField(max_length=100)),
            ],
        ),
    ]