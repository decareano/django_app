# Generated by Django 3.0.4 on 2020-05-11 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidapp', '0007_auto_20200511_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='ICU_currently',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='dead_daily',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_increase',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='tested_today',
            field=models.IntegerField(),
        ),
    ]
