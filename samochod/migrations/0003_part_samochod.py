# Generated by Django 4.2.8 on 2023-12-11 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samochod', '0002_remove_part_samochod_part_bodytype_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='samochod',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
