# Generated by Django 4.2.6 on 2024-03-05 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_art_image_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='image_file',
            field=models.ImageField(blank=True, upload_to='uploaded_images/', verbose_name='Картина'),
        ),
    ]
