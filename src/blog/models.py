from django.db import models
# from django.db.models import Model
from django.utils.encoding import smart_text


PUBLISH_CHOICES = (
    ('draft', 'Draft'),
    ('publish', 'Publish'),
    ('private', 'Private'),
)


class PostModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    # id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=240, verbose_name='Post Title')
    content = models.TextField(null=True, blank=True)
    publish = models.CharField(
        max_length=120, choices=PUBLISH_CHOICES, default='draft')
    active = models.BooleanField(default=True)  # null=True

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return smart_text(self.title)
