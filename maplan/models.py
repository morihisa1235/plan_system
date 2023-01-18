from accounts.models import CustomUser
from django.db import models

# Create your models here.
class Plan(models.Model):
    """プランモデル"""
    #データベースに登録するプランのデータ
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    plan_name = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文', blank=True, null=True)
    photo = models.ImageField(verbose_name='写真', blank=True, null=True)
    memo = models.TextField(verbose_name='メモ', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', blank=True, null=True)
    start_time= models.TimeField(verbose_name='滞在開始時間', blank=True, null=True)
    end_time= models.TimeField(verbose_name='滞在終了時間', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Plan'

    def __str__(self):
        return self.title

class Prefecture(models.Model):
    """都道府県モデル"""
    prefecture_code = models.CharField(verbose_name='都道府県コード', max_length=4, primary_key=True)
    prefecture_name = models.CharField(verbose_name='都道府県名', max_length=4, null=False)

    class Meta:
        verbose_name_plural = 'Prefecture'

    def __str__(self):
        return self.prefecture_name

class Tourism(models.Model):
    """観光名所モデル"""
    tourism_code = models.CharField(verbose_name='観光名所コード', max_length=8, primary_key=True)
    tourism_name = models.TextField(verbose_name="観光名所名", null=False)
    tourism_category = models.TextField(verbose_name="カテゴリー名", null=True)
    address = models.TextField(verbose_name="住所", null=False)
    category_code = models.IntegerField(verbose_name="カテゴリーコード", max_length=2, null=False)
    prefecture_code = models.CharField(verbose_name="都道府県コード", max_length=5, null=False)

    class Meta:
        verbose_name_plural = 'Tourism'

    def __str__(self):
        return self.tourism_name