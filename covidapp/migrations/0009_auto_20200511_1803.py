# Generated by Django 3.0.4 on 2020-05-11 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covidapp', '0008_auto_20200511_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='ICU_currently',
            new_name='icucurrently',
        ),
    ]
