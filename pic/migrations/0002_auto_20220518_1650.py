# Generated by Django 3.2.12 on 2022-05-18 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infor',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='infor',
            name='type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='type',
            name='type',
            field=models.CharField(max_length=50),
        ),
    ]
