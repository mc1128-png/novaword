# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from users.models import UserProfile
# Create your models here.


class UserMessage(models.Model):
    to_user = models.IntegerField(default=0, verbose_name=u"收消息的用户")
    from_user = models.ForeignKey(UserProfile, default=None, verbose_name=u"发送消息的用户")
    message = models.CharField(max_length=500, verbose_name=u"消息内容")
    has_read = models.BooleanField(default=False, verbose_name=u"已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    model_icon = 'fa fa-envelope-open'

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return u"{0} - {1}".format(self.from_user, self.message)
