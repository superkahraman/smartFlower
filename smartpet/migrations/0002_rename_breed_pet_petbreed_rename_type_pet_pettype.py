# Generated by Django 4.0.2 on 2022-02-28 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smartpet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='breed',
            new_name='petbreed',
        ),
        migrations.RenameField(
            model_name='pet',
            old_name='type',
            new_name='pettype',
        ),
    ]
