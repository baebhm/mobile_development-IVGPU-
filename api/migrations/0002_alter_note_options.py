# Generated by Django 5.0.1 on 2024-01-21 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-id']},
        ),
    ]
