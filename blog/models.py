from django.db import models

NULLABLE = {'blank': 'True', 'null': 'True'}


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    body = models.TextField(verbose_name="body")
    preview = models.ImageField(verbose_name="preview", **NULLABLE)
    creation_date = models.DateField(verbose_name="created", auto_now_add=True)
    views = models.IntegerField(verbose_name="views", default=0)
    is_published = models.BooleanField(verbose_name="published", default=True)
    slug = models.CharField(verbose_name="slug", max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
