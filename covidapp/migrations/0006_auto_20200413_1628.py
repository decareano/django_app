# Generated by Django 3.0.4 on 2020-04-13 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidapp', '0005_auto_20200413_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='ICU_currently',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_currently',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='tested_today',
            field=models.TextField(blank=True),
        ),
    ]
