from django.db import models


class Blog(models.Model):

    title = models.CharField(max_length=150, verbose_name='Заголовок')
    data = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='images/blog', blank=True, null=True)
    created_at = models.DateField(verbose_name='Дата создания')
    published = models.BooleanField(default=False, verbose_name='Признак публикации')
    count_view = models.PositiveIntegerField(verbose_name='Количество просмотров', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
