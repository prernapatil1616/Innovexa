# Generated by Django 4.2.5 on 2023-11-24 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_challenge_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='featured_image',
            field=models.ImageField(null=True, upload_to='featured_img'),
        ),
    ]
