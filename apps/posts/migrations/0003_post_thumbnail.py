# Generated by Django 4.2.11 on 2024-04-22 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_deleted_at_post_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.CharField(blank=True, null=True),
        ),
    ]