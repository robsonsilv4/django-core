# Generated by Django 2.1.4 on 2018-12-06 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20181206_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]