# 引入模板，导包
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# 创建模型类并继承models.Model
class Movie(models.Model):
    # 一个类就是数据库的一张表
    # 创建数据库字段  变量名 = models.某个方法（）
    title = models.CharField(max_length=100,verbose_name='电影名')   #CharField字符串字段
    description = models.TextField(max_length=666,verbose_name='电影简介')
    image=models.ImageField(upload_to='movie/images/',verbose_name='电影海报')#ImageField用于保存图像文件的字段
    url = models.URLField(blank=True,verbose_name='电影资源')

    class Meta:
        verbose_name = '电影'
        verbose_name_plural= verbose_name

    def __str__(self):
        return self.title

class Review(models.Model) :
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)#实现多对1的方式，多个评论对应一个用户
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    watchAgain = models.BooleanField()
    def __str__(self) :
        return self.text