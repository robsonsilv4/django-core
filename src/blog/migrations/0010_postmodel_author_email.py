# Generated by Django 2.1.4 on 2018-12-06 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20181203_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='author_email',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
    ]
