# Generated by Django 4.2.8 on 2023-12-12 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samochod', '0003_part_samochod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='samochod',
        ),
    ]