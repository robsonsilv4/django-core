from django.db import models
# from django.db.models import Model


class PostModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    # id = models.IntegerField(primary_key=True)
    active = models.BooleanField(default=True)  # null=True
    pass
