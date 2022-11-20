# Generated by Django 4.1.3 on 2022-11-20 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.AlterModelOptions(
            name='country',
            options={},
        ),
        migrations.AlterModelOptions(
            name='discover',
            options={},
        ),
        migrations.AlterModelOptions(
            name='disease',
            options={},
        ),
        migrations.AlterModelOptions(
            name='diseasetype',
            options={},
        ),
        migrations.AlterModelOptions(
            name='doctor',
            options={},
        ),
        migrations.AlterModelOptions(
            name='publicservant',
            options={},
        ),
        migrations.AlterModelOptions(
            name='record',
            options={},
        ),
        migrations.AlterModelOptions(
            name='specialize',
            options={},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={},
        ),
    ]
