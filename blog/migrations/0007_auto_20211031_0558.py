# Generated by Django 3.1.7 on 2021-10-31 05:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20211031_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
