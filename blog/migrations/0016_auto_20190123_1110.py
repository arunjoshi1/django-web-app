# Generated by Django 2.1.5 on 2019-01-23 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20190123_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(default='featured/default.jpg', upload_to='featured'),
        ),
    ]
