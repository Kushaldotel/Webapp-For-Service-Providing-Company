# Generated by Django 4.1.5 on 2023-02-12 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('try', '0003_contact_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
