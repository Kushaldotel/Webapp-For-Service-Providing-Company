# Generated by Django 4.1.5 on 2023-02-23 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('try', '0006_delete_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=200)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
