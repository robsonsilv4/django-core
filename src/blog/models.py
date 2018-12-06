from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.encoding import smart_text
from django.utils.text import slugify
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
    slug = models.SlugField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    publish = models.CharField(
        max_length=120, choices=PUBLISH_CHOICES, default='draft')
    active = models.BooleanField(default=True)  # null=True
    view_count = models.IntegerField(default=0)
    publish_date = models.DateField(
        auto_now=False, auto_now_add=False, default=timezone.now)
    author_email = models.EmailField(
        max_length=240, null=True, blank=True, validators=[validate_robson])

    def save(self, *args, **kwargs):
        # if not self.slug and self.title:
        #     self.slug = slugify(self.title)
        super(PostModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        # unique_together = [('title', 'slug')]

    def __str__(self):
        return smart_text(self.title)


def blog_post_model_pre_save(sender, instance, *args, **kwargs):
    print('Before Save...')
    if not instance.slug and instance.title:
        instance.slug = slugify(instance.title)
        instance.save()


pre_save.connect(blog_post_model_pre_save, sender=PostModel)


def blog_post_model_post_save(sender, instance, created, *args, **kwargs):
    print('After Save...')
    print(created)
    if created:
        if not instance.slug and instance.title:
            instance.slug = slugify(instance.title)
            instance.save()


post_save.connect(blog_post_model_post_save, sender=PostModel)
