from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=120)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'price': self.price,
            'description': self.description,
            'address': self.address,
            'is_published': self.is_published,
        }


class Category(models.Model):
    name = models.CharField(max_length=200)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }
