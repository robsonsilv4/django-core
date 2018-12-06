from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.encoding import smart_text
from django.utils.text import slugify
from django.utils import timezone
from django.utils.timesince import timesince
from datetime import timedelta, datetime, date

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
        max_length=240,
        unique=True,
        error_messages={
            'unique': 'This Title is not unique, try again!'
        },
        help_text='Must be a unique Title!',
        verbose_name='Post Title'
    )
    slug = models.SlugField(null=True, blank=True)  # editable=False
    content = models.TextField(null=True, blank=True)
    publish = models.CharField(
        max_length=120, choices=PUBLISH_CHOICES, default='draft')
    active = models.BooleanField(default=True)  # null=True
    view_count = models.IntegerField(default=0)
    publish_date = models.DateField(
        auto_now=False, auto_now_add=False, default=timezone.now)
    author_email = models.EmailField(
        max_length=240, null=True, blank=True, validators=[validate_robson])
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

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

    @property
    def age(self):
        if self.publish == 'publish':
            now = datetime.now()
            publish_time = datetime.combine(
                self.publish_date,
                datetime.now().min.time()
            )
            try:
                difference = now - publish_time
            except:
                return 'Unknown'
            if difference <= timedelta(minutes=1):
                return 'Just Now.'
            return '{time} ago.'.format(time=timesince(publish_time).split(', ')[0])
        return 'Not Published!'


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
