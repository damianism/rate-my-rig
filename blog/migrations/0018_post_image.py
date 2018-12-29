# Generated by Django 2.0 on 2018-12-29 12:08

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_post_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, quality=0, size=[500, 500], upload_to='posts_pics'),
        ),
    ]