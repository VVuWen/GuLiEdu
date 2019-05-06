from django.db import models
from datetime import datetime
from apps.users.models import UserProfile #!!!!!!!!!!!!!!!!apps.
from apps.courses.models import CourseInfo #!!!!!!!!!!!!!!!!apps.
# Create your models here.

class UserAsk(models.Model):
    name = models.CharField(max_length=30,verbose_name='姓名')
    phone = models.CharField(max_length=11,verbose_name='手机')
    course = models.CharField(max_length=20,verbose_name='课程')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='咨询时间')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '咨询信息'
        verbose_name_plural = verbose_name

#收藏表，收藏机构，老师，课程，love_id ，love_type两个字段联合起来查询！！！！！！    
class UserLove(models.Model):
    love_man = models.ForeignKey(UserProfile,verbose_name='收藏用户')
    love_id = models.IntegerField(verbose_name='收藏的id')
    love_type = models.IntegerField(choices=(('1','org'),(2,'course'),(3,'teacher')),verbose_name='收藏类别')
    love_status = models.BooleanField(default=False,verbose_name='收藏状态')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='收藏时间')

    def __str__(self):
        return self.love_man.username

    class Meta:
        verbose_name = '收藏信息'
        verbose_name_plural = verbose_name

#用户与课程是多对多的关系，第三张表UserCourse量它们两连接起来！！！！！
class UserCourse(models.Model):
    study_man = models.ForeignKey(UserProfile,verbose_name='学习用户')
    study_course = models.ForeignKey(CourseInfo,verbose_name='学习课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='学习时间')
    
    def __str__(self):
        return self.study_man.username

    class Meta:
        unique_together = ('study_man','study_course') #联合唯一
        verbose_name = '用户学习课程信息'
        verbose_name_plural = verbose_name
        
class UserComment(models.Model):
    comment_man = models.ForeignKey(UserProfile, verbose_name='评论用户')
    comment_course = models.ForeignKey(CourseInfo, verbose_name='评论课程')
    comment_content = models.CharField(max_length=200,verbose_name='评论内容')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='评论时间')

    def __str__(self):
        return self.comment_content

    class Meta:
        verbose_name = '用户评论课程信息'
        verbose_name_plural = verbose_name
        
#用户消息表
class UserMessage(models.Model):
    message_man = models.IntegerField(default=0,verbose_name='消息用户') #mysql中id没0，0代表系统消息给所有人发消息
    message_content = models.CharField(max_length=200,verbose_name='消息内容')
    message_status = models.BooleanField(default=False,verbose_name='消息状态') #默认未读状态
    add_time = models.DateTimeField(default=datetime.now, verbose_name='消息时间')
    
    def __str__(self):
        return self.comment_content

    class Meta:
        verbose_name = '用户消息信息'
        verbose_name_plural = verbose_name
    