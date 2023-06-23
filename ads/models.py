from django.db import models

from users.models import User


class Ad(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.TextField()
    category = models.ForeignKey('ads.Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ad_image', blank=True, null=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author.username,
            'price': self.price,
            'description': self.description,
            'category': self.category.name,
            'is_published': self.is_published,
            'image': self.image.url if self.image else None
        }


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }
