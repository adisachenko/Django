# Generated by Django 3.1.2 on 2020-11-05 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publication',
            field=models.DateField(null=True),
        ),
    ]
