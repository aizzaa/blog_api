from django.db import models
from slugify import slugify
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, primary_key=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()


class Tag(models.Model):
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, primary_key=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name='Автор')
    title =models.CharField(max_length=30, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='posts/', verbose_name='Изображение', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.id}. {self.title}'

