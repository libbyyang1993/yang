# Generated by Django 3.0.6 on 2020-06-03 08:44

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=50, verbose_name='概要')),
                ('description', models.TextField(blank=True, verbose_name='詳細な説明')),
                ('start_time', models.TimeField(default=datetime.time(7, 0), verbose_name='開始時間')),
                ('end_time', models.TimeField(default=datetime.time(7, 0), verbose_name='終了時間')),
                ('date', models.DateField(verbose_name='日付')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='天気の種類')),
                ('created_at', models.TimeField(default=django.utils.timezone.now, verbose_name='日付')),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='タイトル')),
                ('text', models.TextField(verbose_name='本文')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日付')),
                ('attach', models.FileField(default='', upload_to='documents/%Y%m/%d/', verbose_name='添付ファイル')),
                ('weather', models.ManyToManyField(to='employee.Weather', verbose_name='天気(Ctrlで複数選択可)')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, verbose_name='名前')),
                ('text', models.TextField(verbose_name='コメント内容')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日付')),
                ('day', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='employee.Day')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
