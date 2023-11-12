# Generated by Django 4.2 on 2023-11-11 20:14

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'auth_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('entries_limit', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Entries limit per user')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['contest__title', 'style__name'],
            },
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, help_text='will be used in contest URL, can be derrived automatically from titile', unique=True)),
                ('show', models.BooleanField(default=True, verbose_name='Allow to use this category in competitions')),
                ('extra_info_is_required', models.BooleanField(default=False, verbose_name='Require extra information for entries?')),
                ('extra_info_hint', models.CharField(blank=True, help_text='This will instruct the participants what information they need to provide for an entry.</br>Fill only if you require extra information for entries', max_length=255, verbose_name='Required information hint')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_styles', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='modified_styles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'style',
                'verbose_name_plural': 'styles',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('extra_info', models.CharField(blank=True, max_length=1000, verbose_name='Additional information')),
                ('is_paid', models.BooleanField(default=False)),
                ('is_received', models.BooleanField(default=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('brewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='contest.category')),
            ],
            options={
                'verbose_name': 'entry',
                'verbose_name_plural': 'entries',
                'ordering': ['category__contest__title', 'category__style__name', 'brewer', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(blank=True, help_text='will be used in contest URL, can be derrived automatically from titile', unique=True)),
                ('description', models.TextField()),
                ('entry_fee_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('entry_fee_currency', models.CharField(max_length=3, verbose_name='Fee currency code')),
                ('entry_global_limit', models.SmallIntegerField(blank=True, help_text='Leave blank if no limit should be applied', null=True, verbose_name='Limit of entries in the contest')),
                ('entry_user_limit', models.SmallIntegerField(blank=True, help_text='Leave blank if no limit should be applied', null=True, verbose_name='Limit of entries per participant')),
                ('delivery_address', models.TextField(verbose_name='Delivery address')),
                ('registration_date_from', models.DateField(blank=True, null=True, verbose_name='Entry registration from')),
                ('registration_date_to', models.DateField(blank=True, null=True, verbose_name='to')),
                ('delivery_date_from', models.DateField(blank=True, null=True, verbose_name='Delivery from')),
                ('delivery_date_to', models.DateField(blank=True, null=True, verbose_name='to')),
                ('judging_date_from', models.DateField(blank=True, null=True, verbose_name='Judging sessions from')),
                ('judging_date_to', models.DateField(blank=True, null=True, verbose_name='to')),
                ('competition_is_published', models.BooleanField(default=False, help_text='Ignores auto-publish date', verbose_name='Competition page is published')),
                ('competition_autopublish_datetime', models.DateTimeField(blank=True, help_text='Fill only if you want the competition page to be published automatically at that time', null=True, verbose_name='When to publish competition page automatically')),
                ('result_is_published', models.BooleanField(default=False, help_text='Ignores auto-publish date', verbose_name='Competition results are published')),
                ('result_autopublish_datetime', models.DateTimeField(blank=True, help_text='Fill only if you want the competition <b>results</b> to be published automatically at that time', null=True, verbose_name='When to publish results automatically')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_contests', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='modified_contests', to=settings.AUTH_USER_MODEL)),
                ('styles', models.ManyToManyField(through='contest.Category', to='contest.style')),
            ],
            options={
                'verbose_name': 'contest',
                'verbose_name_plural': 'contests',
                'ordering': ('-judging_date_from', '-delivery_date_to'),
            },
        ),
        migrations.AddField(
            model_name='category',
            name='contest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='contest.contest'),
        ),
        migrations.AddField(
            model_name='category',
            name='created_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_categories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='category',
            name='modified_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='modified_categories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='category',
            name='style',
            field=models.ForeignKey(limit_choices_to={'show': True}, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='contest.style'),
        ),
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(fields=('style', 'contest'), name='unique_contest_style'),
        ),
    ]
