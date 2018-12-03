from django.db import models
# from django.db.models import Model


class PostModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    # id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=240, verbose_name='Post Title')
    content = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)  # null=True

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
