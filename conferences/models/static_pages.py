from django.db import models


class StaticPage(models.Model):
    FORMATS = (
        ("html", "HTML"),
        ("txt", "Plain Text"),
        ("md", "Markdown"),
    )
    title = models.CharField(max_length=200, default=None, blank=True, null=True)
    content = models.TextField(default=None, blank=True, null=True)
    format = models.TextField(max_length=4, choices=FORMATS, default="txt")
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'static_pages'
        verbose_name = "StaticPage"
        verbose_name_plural = "static_pages"

    def __str__(self):
        return self.nombre
