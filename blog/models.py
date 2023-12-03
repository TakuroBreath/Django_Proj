from django.db import models

NULLABLE = {'blank': 'True', 'null': 'True'}


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    body = models.TextField(verbose_name="body")
    preview = models.ImageField(verbose_name="preview", **NULLABLE)
    creation_date = models.DateField(verbose_name="created")
    views = models.IntegerField(verbose_name="views")
    published = models.BooleanField(verbose_name="published", default=True)
    slug = models.SlugField(verbose_name="slug")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
