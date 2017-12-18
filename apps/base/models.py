from datetime import datetime

from django.db import models

from material.models import MaterialSocial, MaterialMaster

# Create your models here.


class SiteInfo(models.Model):
    name = models.CharField(default="", max_length=20, verbose_name="名称", help_text="名称")
    name_en = models.CharField(default="", max_length=20, verbose_name="名称英文", help_text="名称英文")
    desc = models.CharField(default="", max_length=20, verbose_name="简介", help_text="简介")
    icon = models.ImageField(upload_to="base/icon/%y/%m", null=True, blank=True, verbose_name="图标", help_text="图标")
    copyright = models.CharField(default="", max_length=100, verbose_name="版权", help_text="版权")
    icp = models.CharField(default="", max_length=20, verbose_name="ICP", help_text="ICP")
    is_live = models.BooleanField(default=False, verbose_name="是否激活", help_text="是否激活")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "网站信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BloggerInfo(models.Model):
    name = models.CharField(default="", max_length=20, verbose_name="名称", help_text="名称")
    name_en = models.CharField(default="", max_length=20, verbose_name="名称英文", help_text="名称英文")
    desc = models.CharField(default="", max_length=300, verbose_name="简介", help_text="简介")
    avatar = models.ImageField(upload_to="base/avatar/%y/%m", null=True, blank=True, verbose_name="头像", help_text="头像")
    background = models.ImageField(upload_to="base/background/%y/%m", null=True, blank=True, verbose_name="背景图", help_text="背景图")
    socials = models.ManyToManyField(MaterialSocial, through='BloggerSocial', through_fields=('blogger', 'social'))
    masters = models.ManyToManyField(MaterialMaster, through='BloggerMaster', through_fields=('blogger', 'master'))
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "个人信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BloggerSocial(models.Model):
    name = models.CharField(default="", max_length=20, verbose_name="名称", help_text="名称")
    blogger = models.ForeignKey(BloggerInfo, verbose_name="个人", help_text="个人")
    social = models.ForeignKey(MaterialSocial, verbose_name="社交平台", help_text="社交平台")
    index = models.IntegerField(default=0, verbose_name="顺序", help_text="顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "社交信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BloggerMaster(models.Model):
    name = models.CharField(default="", max_length=20, verbose_name="名称", help_text="名称")
    blogger = models.ForeignKey(BloggerInfo, verbose_name="个人", help_text="个人")
    master = models.ForeignKey(MaterialMaster, verbose_name="技能", help_text="技能")
    index = models.IntegerField(default=0, verbose_name="顺序", help_text="顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "技能信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class FriendLink(models.Model):
    """
    友情链接
    """
    name = models.CharField(max_length=30, verbose_name="名称", help_text="名称")
    desc = models.CharField(max_length=100, verbose_name="简介", help_text="简介")
    image = models.ImageField(upload_to="base/friendlink/%y/%m", verbose_name="图片", help_text="图片")
    url = models.URLField(max_length=200, verbose_name="链接", help_text="链接")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "友情链接"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name