# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.utils.timezone
import django.contrib.auth.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], error_messages={'unique': 'A user with that username already exists.'}, verbose_name='username', help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, max_length=30)),
                ('first_name', models.CharField(max_length=30, blank=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, blank=True, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, blank=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(verbose_name='staff status', default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(verbose_name='active', default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='user/', max_length=200, blank=True, verbose_name='用户头像', null=True)),
                ('nick_name', models.CharField(max_length=20, blank=True, verbose_name='用户昵称', null=True)),
                ('birthday', models.DateTimeField(null=True, blank=True, verbose_name='用户生日')),
                ('gender', models.CharField(max_length=10, verbose_name='用户性别', choices=[('girl', '女'), ('boy', '男')], default='girl')),
                ('address', models.CharField(max_length=200, blank=True, verbose_name='用户地址', null=True)),
                ('phone', models.CharField(max_length=11, blank=True, verbose_name='用户手机', null=True)),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
                ('groups', models.ManyToManyField(blank=True, verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', to='auth.Group', related_query_name='user')),
                ('user_permissions', models.ManyToManyField(blank=True, verbose_name='user permissions', help_text='Specific permissions for this user.', related_name='user_set', to='auth.Permission', related_query_name='user')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='BannerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('image', models.ImageField(max_length=200, upload_to='banner/', verbose_name='轮播图片')),
                ('url', models.URLField(verbose_name='图片链接', default='http://www.atguigu.com')),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '轮播图信息',
                'verbose_name_plural': '轮播图信息',
            },
        ),
        migrations.CreateModel(
            name='EmailVerifyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=20, verbose_name='邮箱验证码')),
                ('email', models.EmailField(max_length=200, verbose_name='验证码邮箱')),
                ('send_type', models.IntegerField(verbose_name='验证码类型', choices=[(1, 'register'), (2, 'forget'), (3, 'change')])),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '邮箱验证码',
                'verbose_name_plural': '邮箱验证码',
            },
        ),
    ]
