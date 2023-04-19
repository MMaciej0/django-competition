# Generated by Django 4.2 on 2023-04-19 16:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0011_alter_category_options_contest_styles'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['contest__title', 'style__name'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='entries_limit',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Entries limit per user'),
        ),
    ]
