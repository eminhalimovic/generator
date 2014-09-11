# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatabaseConnection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('connection_name', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=256)),
                ('user', models.CharField(max_length=256, blank=True)),
                ('password', models.CharField(max_length=256, blank=True)),
                ('host', models.CharField(max_length=25, blank=True)),
                ('port', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'settings_db_connection',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DatabaseEngine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'settings_db_engine',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoApp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=256)),
            ],
            options={
                'db_table': 'settings_django_apps',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InstalledApp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('installed_app', models.ForeignKey(to='project.DjangoApp')),
            ],
            options={
                'db_table': 'settings_installed_apps',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InstalledMiddlewareClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'settings_installed_middleware_classes',
                'verbose_name_plural': 'Installed Middleware Classes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InstalledStaticfilesFinder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'settings_installed_staticfiles_finders',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InstalledTemplateLoader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'settings_installed_template_loaders',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MiddlewareClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=256)),
            ],
            options={
                'db_table': 'settings_middleware_classes',
                'verbose_name_plural': 'Middleware classes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name', models.CharField(max_length=64)),
                ('home_dir', models.CharField(max_length=1024)),
                ('allowed_hosts', models.CharField(max_length=1024, blank=True)),
                ('debug', models.BooleanField(default=True)),
                ('language_code', models.CharField(max_length=16)),
                ('logging', models.CharField(max_length=1024, blank=True)),
                ('managers', models.CharField(default=b'ADMINS', max_length=1024)),
                ('media_root', models.CharField(max_length=1024, blank=True)),
                ('media_url', models.CharField(max_length=1024, blank=True)),
                ('root_urlconf', models.CharField(default=b'.urls', max_length=1024)),
                ('secret_key', models.CharField(max_length=1024)),
                ('site_id', models.IntegerField(default=1)),
                ('staticfiles_dirs', models.CharField(max_length=1024, blank=True)),
                ('static_root', models.CharField(max_length=1024, blank=True)),
                ('static_url', models.CharField(default=b'/static/', max_length=1024)),
                ('template_debug', models.CharField(default=b'DEBUG', max_length=1024)),
                ('template_dirs', models.CharField(max_length=1024, blank=True)),
                ('time_zone', models.CharField(max_length=64)),
                ('use_i18n', models.BooleanField(default=True)),
                ('use_l10n', models.BooleanField(default=True)),
                ('use_tz', models.BooleanField(default=True)),
                ('wsgi_application', models.CharField(default=b'.wsgi.application', max_length=1024)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectAdmin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=256)),
                ('project', models.ForeignKey(to='project.Project')),
            ],
            options={
                'db_table': 'settings_project_admins',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectDatabase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('connection', models.ForeignKey(to='project.DatabaseConnection')),
                ('project', models.ForeignKey(to='project.Project')),
            ],
            options={
                'db_table': 'settings_database_project',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StaticfilesFinder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=256)),
            ],
            options={
                'db_table': 'settings_staticfiles_finders',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TemplateLoader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=256)),
            ],
            options={
                'db_table': 'settings_template_loaders',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='installedtemplateloader',
            name='installed_template_loader',
            field=models.ForeignKey(to='project.TemplateLoader'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='installedtemplateloader',
            name='project',
            field=models.ForeignKey(to='project.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='installedstaticfilesfinder',
            name='installed_staticfiles_finder',
            field=models.ForeignKey(to='project.StaticfilesFinder'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='installedstaticfilesfinder',
            name='project',
            field=models.ForeignKey(to='project.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='installedmiddlewareclass',
            name='installed_middleware_class',
            field=models.ForeignKey(to='project.MiddlewareClass'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='installedmiddlewareclass',
            name='project',
            field=models.ForeignKey(to='project.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='installedapp',
            name='project',
            field=models.ForeignKey(to='project.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='databaseconnection',
            name='engine',
            field=models.ForeignKey(to='project.DatabaseEngine'),
            preserve_default=True,
        ),
    ]
