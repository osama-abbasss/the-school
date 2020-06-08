from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Blog(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(blank=True, null=True)
    img = models.ImageField(upload_to='blog/')
    detail = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
