# Generated by Django 3.0.3 on 2020-02-06 12:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='vote',
            field=models.CharField(blank=True, choices=[('plus', 'плюс'), ('minus', 'минус'), ('none', 'none')], max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('author', 'content_type', 'object_id', 'vote')},
        ),
    ]
