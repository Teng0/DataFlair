# Generated by Django 3.2.4 on 2021-06-30 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specs',
            name='weight',
            field=models.DecimalField(decimal_places=3, max_digits=7),
        ),
    ]