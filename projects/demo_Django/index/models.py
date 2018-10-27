from django.db import models


# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, verbose_name='名称')
    bpub_date = models.DateField(verbose_name='出版日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=0, verbose_name='逻辑处理')
    image=models.ImageField(upload_to='books',verbose_name='图书图片',null=True)

    class Meta:
        db_table = 'tb_books'
        verbose_name = '图书'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.btitle


class HerroInfo(models.Model):
    GENDER_CHOICES=(
        (0,'male'),
        (1,'female'))
    hname =models.CharField(max_length=20,verbose_name='名称')
    hgender=models.SmallIntegerField(choices=GENDER_CHOICES,default=0,verbose_name='性别')
    hcomment =models.CharField(max_length=200,null=True,verbose_name='描述信息')
    hbook=models.ForeignKey(BookInfo,on_delete=models.CASCADE,verbose_name='图书')
    is_delete =models.BooleanField(default=False,verbose_name='逻辑删除')

    class Meta:
        db_table ='tb_heros'
        verbose_name='英雄'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.hname
