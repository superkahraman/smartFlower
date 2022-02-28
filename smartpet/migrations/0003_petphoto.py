# Generated by Django 4.0.2 on 2022-02-28 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smartpet', '0002_rename_breed_pet_petbreed_rename_type_pet_pettype'),
    ]

    operations = [
        migrations.CreateModel(
            name='petPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=512)),
                ('pet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='smartpet.pet')),
            ],
        ),
    ]