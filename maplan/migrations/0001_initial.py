# Generated by Django 3.2.7 on 2023-02-07 00:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_code', models.IntegerField(primary_key=True, serialize=False, verbose_name='カテゴリーコード')),
                ('category_name', models.CharField(max_length=11, verbose_name='カテゴリー名')),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=40, verbose_name='タイトル')),
                ('content', models.TextField(blank=True, null=True, verbose_name='本文')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='作成日時')),
                ('open', models.IntegerField(verbose_name='公開設定')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'verbose_name_plural': 'Plan',
            },
        ),
        migrations.CreateModel(
            name='Prefecture',
            fields=[
                ('prefecture_code', models.CharField(max_length=4, primary_key=True, serialize=False, verbose_name='都道府県コード')),
                ('prefecture_name', models.CharField(max_length=4, verbose_name='都道府県名')),
            ],
            options={
                'verbose_name_plural': 'Prefecture',
            },
        ),
        migrations.CreateModel(
            name='Tourism',
            fields=[
                ('tourism_code', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='観光名所コード')),
                ('tourism_name', models.TextField(verbose_name='観光名所名')),
                ('address', models.TextField(verbose_name='住所')),
                ('prefecture_code', models.CharField(max_length=5, verbose_name='都道府県コード')),
                ('category_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='maplan.category', verbose_name='カテゴリーコード')),
            ],
            options={
                'verbose_name_plural': 'Tourism',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(null=True, verbose_name='滞在時間')),
                ('start_time', models.TimeField(blank=True, null=True, verbose_name='滞在開始時間')),
                ('end_time', models.TimeField(blank=True, null=True, verbose_name='滞在終了時間')),
                ('plan_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='maplan.plan', verbose_name='プラン名')),
                ('tourism_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='maplan.tourism', verbose_name='観光名所名')),
            ],
            options={
                'verbose_name_plural': 'Route',
            },
        ),
        migrations.CreateModel(
            name='Plan_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='maplan.category', verbose_name='カテゴリーコード')),
                ('plan_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='maplan.plan', verbose_name='プランID')),
            ],
            options={
                'verbose_name_plural': 'Plan_category',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='コメント')),
                ('evalution', models.IntegerField(verbose_name='評価')),
                ('plan_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='maplan.plan', verbose_name='プランID')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'verbose_name_plural': 'Comment',
            },
        ),
    ]
