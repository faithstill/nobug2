# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin


# Create your models here.
# 这个文章的类模板
class NewsPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField()


# 这是改进admin界面的类模板
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

# 这个是干啥的？
admin.site.register(NewsPost,NewsPostAdmin)
