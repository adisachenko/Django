# Generated by Django 3.1.2 on 2020-11-09 14:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_remove_book_publication'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publication',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
