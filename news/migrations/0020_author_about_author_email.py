# Generated by Django 5.0.4 on 2024-05-30 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0019_alter_post_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='about',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
