# Generated by Django 4.2.8 on 2023-12-11 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samochod', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='samochod',
        ),
        migrations.AddField(
            model_name='part',
            name='bodyType',
            field=models.CharField(choices=[('sedan', 'Sedan'), ('kombi', 'Kombi'), ('hatchback', 'Hatchback'), ('cabriolet', 'Kabriolet'), ('coupe', 'Coupe')], default='sedan', max_length=255),
        ),
        migrations.AddField(
            model_name='part',
            name='endOfProduction',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='part',
            name='engines',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='part',
            name='mark',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='part',
            name='model',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='part',
            name='startOfProduction',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Samochod',
        ),
    ]