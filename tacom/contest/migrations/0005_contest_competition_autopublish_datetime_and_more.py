# Generated by Django 4.2 on 2023-04-13 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0004_alter_contest_created_by_alter_contest_modified_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='competition_autopublish_datetime',
            field=models.DateTimeField(blank=True, help_text='Fill only if you want the competition page to be published automatically at that time', null=True, verbose_name='When to publish competition page automatically'),
        ),
        migrations.AddField(
            model_name='contest',
            name='competition_is_published',
            field=models.BooleanField(default=False, help_text='Ignores auto-publish date', verbose_name='Competition page is published'),
        ),
        migrations.AddField(
            model_name='contest',
            name='delivery_date_from',
            field=models.DateField(blank=True, null=True, verbose_name='Delivery from'),
        ),
        migrations.AddField(
            model_name='contest',
            name='delivery_date_to',
            field=models.DateField(blank=True, null=True, verbose_name='to'),
        ),
        migrations.AddField(
            model_name='contest',
            name='judging_date_from',
            field=models.DateField(blank=True, null=True, verbose_name='Judging sessions from'),
        ),
        migrations.AddField(
            model_name='contest',
            name='judging_date_to',
            field=models.DateField(blank=True, null=True, verbose_name='to'),
        ),
        migrations.AddField(
            model_name='contest',
            name='registration_date_from',
            field=models.DateField(blank=True, null=True, verbose_name='Entry registration from'),
        ),
        migrations.AddField(
            model_name='contest',
            name='registration_date_to',
            field=models.DateField(blank=True, null=True, verbose_name='to'),
        ),
        migrations.AddField(
            model_name='contest',
            name='result_autopublish_datetime',
            field=models.DateTimeField(blank=True, help_text='Fill only if you want the competition <b>results</b> to be published automatically at that time', null=True, verbose_name='When to publish results automatically'),
        ),
        migrations.AddField(
            model_name='contest',
            name='result_is_published',
            field=models.BooleanField(default=False, help_text='Ignores auto-publish date', verbose_name='Competition results are published'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='slug',
            field=models.SlugField(blank=True, help_text='will be used in contest URL, can be derrived automatically from titile', unique=True),
        ),
    ]
