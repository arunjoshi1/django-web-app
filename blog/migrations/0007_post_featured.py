# Generated by Django 2.1.5 on 2019-01-22 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.ImageField(blank=True, default='featured.png', upload_to=''),
        ),
    ]
