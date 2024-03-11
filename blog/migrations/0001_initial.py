# Generated by Django 4.2.9 on 2024-03-10 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
                ('content', models.TextField(verbose_name='Содержимое')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Изображение')),
                ('created_at', models.DateField(auto_now=True, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликован')),
                ('count_views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
    ]
