# Generated by Django 3.2.3 on 2022-04-07 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20220401_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='image',
            field=models.CharField(max_length=600),
        ),
    ]
