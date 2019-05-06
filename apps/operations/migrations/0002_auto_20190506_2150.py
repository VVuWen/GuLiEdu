# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
        ('operations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlove',
            name='love_man',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='收藏用户'),
        ),
        migrations.AddField(
            model_name='usercourse',
            name='study_course',
            field=models.ForeignKey(to='courses.CourseInfo', verbose_name='学习课程'),
        ),
        migrations.AddField(
            model_name='usercourse',
            name='study_man',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='学习用户'),
        ),
        migrations.AddField(
            model_name='usercomment',
            name='comment_course',
            field=models.ForeignKey(to='courses.CourseInfo', verbose_name='评论课程'),
        ),
        migrations.AddField(
            model_name='usercomment',
            name='comment_man',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='评论用户'),
        ),
        migrations.AlterUniqueTogether(
            name='usercourse',
            unique_together=set([('study_man', 'study_course')]),
        ),
    ]
