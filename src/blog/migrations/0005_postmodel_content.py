# Generated by Django 2.1.3 on 2018-12-03 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_postmodel_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
