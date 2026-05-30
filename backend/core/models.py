from django.db import models
from django.utils.text import slugify
import random
import string

def generate_random_slug(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class Short_link(models.Model):
    link = models.URLField()
    short = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.short:
            self.short = generate_random_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.link
