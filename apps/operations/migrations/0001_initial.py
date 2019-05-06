# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('phone', models.CharField(max_length=11, verbose_name='手机')),
                ('course', models.CharField(max_length=20, verbose_name='课程')),
                ('add_time', models.DateTimeField(verbose_name='咨询时间', default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '咨询信息',
                'verbose_name_plural': '咨询信息',
            },
        ),
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('comment_content', models.CharField(max_length=200, verbose_name='评论内容')),
                ('add_time', models.DateTimeField(verbose_name='评论时间', default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '用户评论课程信息',
                'verbose_name_plural': '用户评论课程信息',
            },
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('add_time', models.DateTimeField(verbose_name='学习时间', default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '用户学习课程信息',
                'verbose_name_plural': '用户学习课程信息',
            },
        ),
        migrations.CreateModel(
            name='UserLove',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('love_id', models.IntegerField(verbose_name='收藏的id')),
                ('love_type', models.IntegerField(verbose_name='收藏类别', choices=[('1', 'org'), (2, 'course'), (3, 'teacher')])),
                ('love_status', models.BooleanField(verbose_name='收藏状态', default=False)),
                ('add_time', models.DateTimeField(verbose_name='收藏时间', default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '收藏信息',
                'verbose_name_plural': '收藏信息',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('message_man', models.IntegerField(verbose_name='消息用户', default=0)),
                ('message_content', models.CharField(max_length=200, verbose_name='消息内容')),
                ('message_status', models.BooleanField(verbose_name='消息状态', default=False)),
                ('add_time', models.DateTimeField(verbose_name='消息时间', default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '用户消息信息',
                'verbose_name_plural': '用户消息信息',
            },
        ),
    ]
