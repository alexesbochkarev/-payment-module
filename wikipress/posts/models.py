from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Имя')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Адрес')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title
        

class Post(models.Model):
    text = models.TextField('Текст поста', help_text='Введите текст поста')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='posts',
                               verbose_name='Автор')
    group = models.ForeignKey(Group,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True,
                              related_name='posts',
                              verbose_name='Группа',
                              help_text='Выберете группу')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    image = models.ImageField('Картинка', upload_to='posts/', blank=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        LEN_OF_POST = 15
        return self.text[:LEN_OF_POST]