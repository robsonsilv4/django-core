# Generated by Django 2.1.3 on 2018-12-03 13:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20181203_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='publish_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postmodel',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
