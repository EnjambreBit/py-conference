from django.db import models
from django.template import Context, Template
import markdown as md


class StaticPage(models.Model):
    FORMATS = (
        ("html", "HTML"),
        ("txt", "Plain Text"),
        ("md", "Markdown"),
    )
    title = models.CharField(max_length=200, default=None, blank=True, null=True)
    slug = models.SlugField(
        max_length=100, unique=True, default=None, blank=True, null=True
    )
    content = models.TextField(default=None, blank=True, null=True)
    format = models.TextField(max_length=4, choices=FORMATS, default="txt")
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "static_pages"
        verbose_name = "Static page"
        verbose_name_plural = "static pages"

    def __str__(self):
        return self.title

    def rendered_content(self):
        result = Template(self.content).render(Context({}))
        if self.format == "md":
            result = md.markdown(result, extensions=["tables"])
        return result
