from accounts.models import CustomUser
from django.db import models

# Create your models here.
class Category(models.Model):
    category_code = models.IntegerField(verbose_name="カテゴリーコード", primary_key=True)
    category_name = models.CharField(verbose_name="カテゴリー名",max_length=11, null=False)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.category_name

class Plan(models.Model):
    """プランモデル"""
    #データベースに登録するプランのデータ
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    plan_name = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文', blank=True, null=True)
    photo = models.ImageField(verbose_name='写真', blank=True, null=True)
    category_code = models.ForeignKey(Category, verbose_name='カテゴリーコード', on_delete=models.PROTECT)
    created_at = models.DateTimeField(verbose_name='作成日時', blank=True, null=True)
    open = models.IntegerField(verbose_name='公開設定', null=False)

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
    address = models.TextField(verbose_name="住所", null=False)
    category_code = models.ForeignKey(Category, verbose_name="カテゴリーコード", null=False, on_delete=models.PROTECT)
    prefecture_code = models.CharField(verbose_name="都道府県コード", max_length=5, null=False)

    class Meta:
        verbose_name_plural = 'Tourism'

    def __str__(self):
        return self.tourism_name

class Route(models.Model):
    plan_code = models.ForeignKey(Plan, verbose_name="プラン名", null=False, on_delete=models.PROTECT)
    tourism_code = models.ForeignKey(Tourism, verbose_name="観光名所名", null=False, on_delete=models.PROTECT)
    time = time = models.TimeField(verbose_name="滞在時間", null=True)
    start_time= models.TimeField(verbose_name='滞在開始時間', blank=True, null=True)
    end_time= models.TimeField(verbose_name='滞在終了時間', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Route'

    def __str__(self):
        return self.id

class Comment(models.Model):
    comment = models.TextField(verbose_name="コメント", null=False)
    user_id = models.ForeignKey(CustomUser, verbose_name="ユーザー", on_delete=models.PROTECT)
    plan_id = models.ForeignKey(Plan, verbose_name="プランID", on_delete=models.PROTECT)
    evalution = models.IntegerField(verbose_name="評価", null=False)

    class Meta:
        verbose_name_plural = 'Comment'

    def __str__(self):
        return self.comment