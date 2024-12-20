# Generated by Django 5.1.3 on 2024-11-27 03:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0002_alter_member_tel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('hit', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now=True)),
                ('file', models.ImageField(height_field=300, null=True, upload_to='board')),
                ('group', models.IntegerField(null=True)),
                ('step', models.IntegerField(default=0)),
                ('indent', models.IntegerField(default=0)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='member.member')),
            ],
        ),
    ]
