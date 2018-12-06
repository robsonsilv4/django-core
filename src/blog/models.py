from django.db import models
# from django.db.models import Model
from django.utils.encoding import smart_text
from django.utils import timezone

from .validators import validate_author_email, validate_robson


PUBLISH_CHOICES = (
    ('draft', 'Draft'),
    ('publish', 'Publish'),
    ('private', 'Private'),
)


class PostModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    # id = models.IntegerField(primary_key=True)
    title = models.CharField(
        max_length=240, unique=True, verbose_name='Post Title')
    content = models.TextField(null=True, blank=True)
    publish = models.CharField(
        max_length=120, choices=PUBLISH_CHOICES, default='draft')
    active = models.BooleanField(default=True)  # null=True
    view_count = models.IntegerField(default=0)
    publish_date = models.DateField(
        auto_now=False, auto_now_add=False, default=timezone.now)
    author_email = models.EmailField(
        max_length=240, null=True, blank=True, validators=[validate_robson])

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        # unique_together = [('title', 'slug')]

    def __str__(self):
        return smart_text(self.title)
