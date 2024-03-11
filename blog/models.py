from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='Содержимое')
    photo = models.ImageField(upload_to='blog/', verbose_name='Изображение', **NULLABLE)
    created_at = models.DateField(auto_now=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')
    count_views = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
