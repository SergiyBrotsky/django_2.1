from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50,verbose_name='товар')
    content = models.TextField(null=True, blank=True,verbose_name='описание')
    price = models.FloatField(null=True, blank=True,verbose_name='цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True,verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
    class Meta:
        verbose_name_plural='Обявления'
        verbose_name='обявление'
        ordering = ['-published']

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True,verbose_name='название')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='Рубрики '
        verbose_name='Рубрика'
        ordering = ['name']

# Create your models here.
