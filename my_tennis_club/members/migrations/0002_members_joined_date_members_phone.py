# Generated by Django 4.2.5 on 2023-10-02 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='members',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]