# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('image', models.ImageField(max_length=200, upload_to='course/', verbose_name='课程封面')),
                ('name', models.CharField(max_length=20, verbose_name='课程名称')),
                ('study_time', models.IntegerField(verbose_name='学习时长', default=0)),
                ('study_num', models.IntegerField(verbose_name='学习人数', default=0)),
                ('level', models.CharField(max_length=5, verbose_name='课程难度', choices=[('gj', '高级'), ('zj', '中级'), ('cj', '初级')], default='cj')),
                ('love_num', models.IntegerField(verbose_name='收藏数', default=0)),
                ('click_num', models.IntegerField(verbose_name='访问量', default=0)),
                ('desc', models.CharField(max_length=200, verbose_name='课程简介')),
                ('detail', models.TextField(verbose_name='课程详情')),
                ('category', models.CharField(max_length=5, verbose_name='课程类别', choices=[('qd', '前端开发'), ('hd', '后端开发')])),
                ('course_notice', models.CharField(max_length=200, verbose_name='课程公告')),
                ('course_need', models.CharField(max_length=100, verbose_name='课程须知')),
                ('teacher_tell', models.CharField(max_length=100, verbose_name='老师教导')),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
                ('orgInfo', models.ForeignKey(to='orgs.OrgInfo', verbose_name='所属机构')),
                ('teacherInfo', models.ForeignKey(to='orgs.TeacherInfo', verbose_name='所属讲师')),
            ],
            options={
                'verbose_name': '课程信息',
                'verbose_name_plural': '课程信息',
            },
        ),
        migrations.CreateModel(
            name='LessonInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='章节名称')),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
                ('courseinfo', models.ForeignKey(to='courses.CourseInfo', verbose_name='所属课程')),
            ],
            options={
                'verbose_name': '章节信息',
                'verbose_name_plural': '章节信息',
            },
        ),
        migrations.CreateModel(
            name='SourceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='资源名称')),
                ('down_load', models.FileField(max_length=200, upload_to='source/', verbose_name='下载路径')),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
                ('courseinfo', models.ForeignKey(to='courses.CourseInfo', verbose_name='所属课程')),
            ],
            options={
                'verbose_name': '资源信息',
                'verbose_name_plural': '资源信息',
            },
        ),
        migrations.CreateModel(
            name='VideoInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='视频名称')),
                ('study_time', models.IntegerField(verbose_name='视频时长', default=0)),
                ('url', models.URLField(verbose_name='视频链接', default='http://atguigu.com')),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
                ('lessoninfo', models.ForeignKey(to='courses.LessonInfo', verbose_name='所属章节')),
            ],
            options={
                'verbose_name': '视频信息',
                'verbose_name_plural': '视频信息',
            },
        ),
    ]
