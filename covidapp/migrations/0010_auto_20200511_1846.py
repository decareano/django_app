# Generated by Django 3.0.4 on 2020-05-11 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidapp', '0009_auto_20200511_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='dead_daily',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_currently',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_increase',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='icucurrently',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='tested_today',
            field=models.IntegerField(null=True),
        ),
    ]
