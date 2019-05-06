# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='城市名称')),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '城市信息',
                'verbose_name_plural': '城市信息',
            },
        ),
        migrations.CreateModel(
            name='OrgInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('image', models.ImageField(max_length=200, upload_to='org/', verbose_name='机构名称')),
                ('name', models.CharField(max_length=20, verbose_name='机构名称')),
                ('course_name', models.IntegerField(verbose_name='课程数', default=0)),
                ('study_num', models.IntegerField(verbose_name='学习人数', default=0)),
                ('address', models.CharField(max_length=200, verbose_name='机构地址')),
                ('desc', models.CharField(max_length=200, verbose_name='机构简介')),
                ('detail', models.TextField(verbose_name='机构详情')),
                ('love_num', models.IntegerField(verbose_name='收藏数', default=0)),
                ('click_num', models.IntegerField(verbose_name='访问量', default=0)),
                ('category', models.CharField(max_length=10, verbose_name='机构类别', choices=[('pxjg', '培训机构'), ('gx', '高校'), ('gr', '个人')])),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
                ('cityinfor', models.ForeignKey(to='orgs.CityInfo', verbose_name='所在城市')),
            ],
            options={
                'verbose_name': '机构信息',
                'verbose_name_plural': '机构信息',
            },
        ),
        migrations.CreateModel(
            name='TeacherInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('image', models.ImageField(max_length=200, upload_to='teacher/', verbose_name='讲师头像')),
                ('name', models.CharField(max_length=20, verbose_name='讲师姓名')),
                ('work_year', models.IntegerField(verbose_name='工作年限', default=3)),
                ('work_position', models.CharField(max_length=20, verbose_name='工作职位')),
                ('work_style', models.CharField(max_length=20, verbose_name='教学特点')),
                ('age', models.IntegerField(verbose_name='讲师年龄', default=30)),
                ('gender', models.CharField(max_length=10, verbose_name='讲师性别', choices=[('boy', '男'), ('girl', '女')], default='boy')),
                ('love_num', models.IntegerField(verbose_name='收藏数', default=0)),
                ('click_num', models.IntegerField(verbose_name='访问量', default=0)),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
                ('work_company', models.ForeignKey(to='orgs.OrgInfo', verbose_name='所属机构')),
            ],
            options={
                'verbose_name': '讲师信息',
                'verbose_name_plural': '讲师信息',
            },
        ),
    ]
