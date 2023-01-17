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