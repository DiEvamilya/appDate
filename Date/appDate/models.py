from django.db import models

from django.utils.text import slugify


class Profile(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    age = models.IntegerField()
    hobbies = models.CharField(max_length=100)
    favorite_music = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.login)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.login
