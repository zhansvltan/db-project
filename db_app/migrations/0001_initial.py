# Generated by Django 4.1.3 on 2022-11-20 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('cname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('population', models.BigIntegerField()),
            ],
            options={
                'db_table': 'country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('disease_code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('pathogen', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'disease',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Diseasetype',
            fields=[
                ('did', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'diseasetype',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=40)),
                ('salary', models.IntegerField()),
                ('phone', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Discover',
            fields=[
                ('cname', models.OneToOneField(db_column='cname', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='db_app.country')),
                ('first_enc_date', models.DateField()),
            ],
            options={
                'db_table': 'discover',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('email', models.OneToOneField(db_column='email', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='db_app.users')),
                ('degree', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'doctor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Publicservant',
            fields=[
                ('email', models.OneToOneField(db_column='email', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='db_app.users')),
                ('department', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'publicservant',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Specialize',
            fields=[
                ('sid', models.OneToOneField(db_column='sid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='db_app.diseasetype')),
            ],
            options={
                'db_table': 'specialize',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('email', models.OneToOneField(db_column='email', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='db_app.publicservant')),
                ('total_deaths', models.IntegerField()),
                ('total_patients', models.IntegerField()),
            ],
            options={
                'db_table': 'record',
                'managed': False,
            },
        ),
    ]
