# Generated by Django 2.1.4 on 2018-12-06 00:48

import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_postmodel_author_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='author_email',
            field=models.EmailField(blank=True, max_length=240, null=True, validators=[blog.validators.validate_robson]),
        ),
    ]
